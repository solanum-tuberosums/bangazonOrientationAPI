"""
bangazon api serializer configuration for order
"""

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bangazon.api.models.model_order import *

class OrderSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Converts the order database table to python data types.

	We exclude no fields.

	Author: Jeremy Bakker
	"""
	class Meta:
		model = Order
		exclude = ()