"""
bangazon api view configuration for product type
"""

from rest_framework import viewsets
from bangazon.api.serializers.serializer_product_type import ProductTypeSerializer
from bangazon.api.models.model_product_type import ProductType


class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product type data to be viewed or edited

    Author: Adam Myers
    """

    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
