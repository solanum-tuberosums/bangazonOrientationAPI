
from rest_framework import viewsets


from bangazon.api.serializers.serializer_product import ProductSerializer
from bangazon.api.models.model_product import Product



class ProductViewSet(viewsets.ModelViewSet):
    """
    ProductViewSet
    - Author: Will Sims
    - Purpose: API endpoint that allows ALL Products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





