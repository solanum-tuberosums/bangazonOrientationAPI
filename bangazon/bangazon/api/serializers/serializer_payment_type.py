from rest_framework import serializers
from bangazon.api.models.model_payment_type import *


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentType
        fields = ('url', 'accountLabel', 'accountType', 'accountNumber')
        depth = 1