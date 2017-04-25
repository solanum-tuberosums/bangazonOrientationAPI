"""
bangazon api view configuration for order
"""

from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows order data to be viewed or edited.

    Author: Jeremy Bakker
    """
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer