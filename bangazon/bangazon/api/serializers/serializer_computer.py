
"""
bangazon api serializer configuration for computer
"""

from rest_framework import serializers
from bangazon.api.models.model_computer import *


class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Converts the computer database table to python data types.

    We exclude no fields.

    Author: Zak Spence
    """
    class Meta:
        model = Computer
        exclude = ()

