"""
bangazon api serializer configuration for employee_training
"""

from rest_framework import serializers
from bangazon.api.models import *


class EmployeeTrainingSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the employee_training model database table into Python data types.

    We exclude no fields.

    Author: Zak Spence
    """

    class Meta:
        model = EmployeeTraining
        exclude = ()