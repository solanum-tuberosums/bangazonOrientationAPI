"""
bangazon api serializer configuration for product type
"""

from rest_framework import serializers

from bangazon.api.models import ProductType
# from api.serializers import ProductSerializer

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the product type database table into Python data types

    We exclude no fields.

    Author: Adam Myers
    """
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = ProductType
        exclude = ()
