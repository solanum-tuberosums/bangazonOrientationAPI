"""
bangazon api view configuration for customer
"""

from rest_framework import viewsets
from bangazon.api.serializers import CustomerSerializer, AdminCustomerSerializer
from bangazon.api.models import *




class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customer data to be viewed or edited

    Author: Zak Spence
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return AdminCustomerSerializer
        else:
            return CustomerSerializer
