"""
bangazon api serializer configuration for customer
"""

from rest_framework import serializers
from bangazon.api.models import *


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the customer model database table into Python datatypes.

    We exclude no fields.

    Author: Zak Spence
    """

    class Meta:
        model = Customer
        exclude = ()