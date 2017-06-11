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

    price = serializers.DecimalField(decimal_places=2, max_digits=10)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField( read_only=True)
    customer = serializers.CharField(source='customer.first_name', read_only=True)
    product_type = serializers.CharField(source='product_type.title', read_only=True)
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    class Meta:
        model = Product
        exclude = ()



