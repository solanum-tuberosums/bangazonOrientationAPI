"""
bangazon api view configuration for customer
"""

from rest_framework import viewsets
from bangazon.api.serializers import serializer_customer
from bangazon.api.models import model_customer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customer data to be viewed or edited

    Author: Zak Spence
    """

    queryset = model_customer.Customer.objects.all()
    serializer_class = serializer_customer.CustomerSerializer
