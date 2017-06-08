"""
bangazon api serializer configuration for payment type
"""

from rest_framework import serializers
from bangazon.api.models import *


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
	"""
	This class converts the payment type model database table into Python data types.

	We exclude no fields.

	Author: Blaise Roberts
	"""
	customer_id = serializers.IntegerField(source='customer_id.id', read_only=True)


	class Meta:
		model = PaymentType
		exclude = ()