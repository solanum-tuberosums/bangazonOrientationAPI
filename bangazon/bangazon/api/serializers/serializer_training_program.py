"""
bangazon api serializer Configuration for training program
"""

from rest_framework import serializers
from bangazon.api.models.model_training_program import *

class TrainingProgramSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts database tables into Python data types

    We exclude no fields.

    Author:
        Adam Myers
    """
    class Meta:
        model = TrainingProgram
        exclude = ()