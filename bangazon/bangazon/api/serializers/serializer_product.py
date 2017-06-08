"""
bangazon api serializer configuration for product
"""

from rest_framework import serializers
from bangazon.api.models import *

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the product model database table into Python data types.

	We exclude no fields.
	
	Author: Will Sims
    """
    product_type = serializers.CharField(source='product_type.label', read_only=True)
    customer = serializers.CharField(source='customer.first_name', read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'