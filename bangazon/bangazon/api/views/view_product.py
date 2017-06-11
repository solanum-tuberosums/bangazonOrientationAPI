"""
bangazon api view configuration for product
"""

from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *
from rest_framework import generics

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import authentication, permissions

import json
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse

#############
## Classes ##
#############


# All products
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product data to be viewed or edited

    Author: Will Sims
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer




# View Products within a certain product type
class ProductsInTypeViewSet(generics.ListAPIView):
    serializer_class = ProductTypeSerializer
    model = Product

    def get_queryset(self):
        type_id = self.request.query_params.get('type_id', None)
        return Product.objects.filter(product_type=type_id)


@api_view(['GET', 'PUT', 'DELETE'])
def ProductDetailViewSet(request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ProductSerializer(product, context={'request': request})
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            print("\n\n\n\nDELETEING\n\n\n\n\n")
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



class ProductView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        product = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        
        req_body = json.loads(request.body.decode())

        fake_customer = Customer.objects.get(pk=1)
        product_type_pk = int(req_body['product_type'][0]);
        product_type = ProductType.objects.get(pk=product_type_pk)


        new_product = Product.objects.create(
            price = req_body['price'],
            title = req_body['title'],
            description = req_body['description'],
            product_type = product_type,
            customer = fake_customer
        )

        token = Token.objects.get(user=request.user)
        print("\n\n\n{}\n\n".format(token.key))
        data = json.dumps({'token':token.key})
        print("\n\nData:{}\n\n".format(data))

        try:
            new_product.save()
            return Response(data, content_type='application/json')
        except:
            print('\n\nuh oh \n\n', new_product)
            return Response(status=status.HTTP_400_BAD_REQUEST)
