"""
bangazon api serializer configuration for payment type
"""

from rest_framework import serializers
from bangazon.api.models.model_payment_type import PaymentType


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
	"""
	This class converts the payment type model database table into Python data types.

	We exclude no fields.

	Author: Blaise Roberts
	"""

	class Meta:
		model = PaymentType
		exclude = ()