"""
bangazon api view configuration for payment type
"""

from rest_framework import viewsets
from bangazon.api.serializers.serializer_payment_type import *
from bangazon.api.models.model_payment_type import *


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows payment type data to be viewed or edited

    Author: Blaise Roberts
    """

    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer