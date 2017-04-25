"""
bangazon api serializer configuration for order
"""

from rest_framework import serializers
from bangazon.api.models.model_order import *


class OrderSerializer(serializers.HyperlinkedModelSerializer):
	"""
	This class converts the order model database table into Python data types.

	We exclude no fields.

	Author: Jeremy Bakker
	"""

	class Meta:
		model = Order
		exclude = ()