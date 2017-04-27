"""
bangazon api view configuration for customer support ticket
"""

from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *


class CustomerSupportTicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customer supoort ticket data to be viewed or edited

    Author: Adam Myers
    """

    queryset = CustomerSupportTicket.objects.all()
    serializer_class = CustomerSupportTicketSerializer