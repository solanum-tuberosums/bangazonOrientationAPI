"""
bangazon api serializer configuration for product
"""

from rest_framework import serializers
from bangazon.api.models import *
from rest_framework.renderers import JSONRenderer

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the product model database table into Python data types.

	We exclude no fields.
	
	Author: Will Sims
    """

    customer = serializers.CharField(source='customer.first_name', read_only=True)
    product_type = serializers.EmailField(source='product_type.label', read_only=True)
    class Meta:
        model = Product
        exclude = ()
        depth = 1