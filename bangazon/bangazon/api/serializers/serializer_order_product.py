"""
bangazon api serializer configuration for order_product
"""

from rest_framework import serializers
from bangazon.api.models import *


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the order_product model database table into Python data types.

    We exclude no fields.

    Author: Zak Spence
    """

    class Meta:
        model = OrderProduct
        exclude = ()