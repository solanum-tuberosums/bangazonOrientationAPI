"""
bangazon api serializer configuration for customer support ticket
"""

from rest_framework import serializers
from bangazon.api.models import *


class CustomerSupportTicketSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the customer support ticket model database table into Python data types.

    We exclude no fields.

    Author: Adam Myers
    """

    class Meta:
        model = CustomerSupportTicket
        exclude = ()