"""
bangazon api view configuration for product type
"""

from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *



class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product type data to be viewed or edited

    Author: Adam Myers
    """

    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

