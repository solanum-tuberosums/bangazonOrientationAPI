"""
bangazon api view configuration for order
"""

from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *
from rest_framework import generics

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows order data to be viewed or edited.

    Author: Jeremy Bakker
    """
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserOrderViewSet(generics.ListAPIView):
    serializer_class = OrderSerializer
    model = Order

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        return Order.objects.get(customer_id=user_id)

