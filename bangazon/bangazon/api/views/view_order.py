"""
bangazon api view configuration for order
"""

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from bangazon.api.serializers.serializer_order import *
from bangazon.api.models.model_order import *
from bangazon.api.models import model_customer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ALL orders to be viewed or edited.

    Author: Jeremy Bakker
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer