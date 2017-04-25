"""
bangazon api serializer configuration for computer
"""

from rest_framework import serializers
from bangazon.api.models import *


class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the computer model database table into Python data types.

    We exclude no fields.

    Author: Zak Spence
    """

    class Meta:
        model = Computer
        exclude = ()