"""
bangazon api serializer configuration for training program
"""

from rest_framework import serializers
from bangazon.api.models import *


class TrainingProgramSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the training program model database table into Python data types

    We exclude no fields.

    Author: Adam Myers
    """

    class Meta:
        model = TrainingProgram
        exclude = ()