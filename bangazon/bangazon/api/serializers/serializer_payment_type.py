"""
bangazon api serializer configuration for payment type
"""
from rest_framework import serializers
from bangazon.api.models.model_payment_type import PaymentType


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Converts the PaymentType into python data types. Excluding no fields.
	Author: Blaise Roberts
	'''
	class Meta:
		model = PaymentType
		exclude = ()