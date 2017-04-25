"""
bangazon api serializer configuration for product
"""

from rest_framework import serializers
from bangazon.api.models.model_product import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the product model database table into Python data types.

	We exclude no fields.
	
	Author: Will Sims
    """

    class Meta:
        model = Product
        exclude = ()




