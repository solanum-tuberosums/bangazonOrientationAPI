"""
bangazon api serializer configuration for product type
"""

from rest_framework import serializers
from bangazon.api.models.model_product_type import ProductType

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the product type database table into Python data types

    We exclude no fields.

    Author: Adam Myers
    """
    class Meta:
        model = ProductType
        exclude = ()
