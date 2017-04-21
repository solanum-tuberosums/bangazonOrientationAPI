"""
bangazon api serializer Configuration for product type
"""

from rest_framework import serializers
from bangazon.api.models.model_product_type import *

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
	"""
	This class converts database tables into Python data types

	We exclude no fields.

	Author:
		Adam Myers
	"""
    class Meta:
        model = ProductType
        exclude = ()