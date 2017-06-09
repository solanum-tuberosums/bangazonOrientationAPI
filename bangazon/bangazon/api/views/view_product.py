"""
bangazon api view configuration for product
"""

from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *
from rest_framework import generics

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product data to be viewed or edited

    Author: Will Sims
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductsInTypeViewSet(generics.ListAPIView):
    serializer_class = ProductTypeSerializer
    model = Product

    def get_queryset(self):
        type_id = self.request.query_params.get('type_id', None)
        return Product.objects.filter(product_type=type_id)
