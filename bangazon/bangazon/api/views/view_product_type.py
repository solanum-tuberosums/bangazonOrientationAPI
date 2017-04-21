from rest_framework import viewsets
from bangazon.api.serializers.serializer_product_type import *
from bangazon.api.models.model_product_type import *

class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer