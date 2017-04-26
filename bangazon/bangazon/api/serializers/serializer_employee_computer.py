"""
bangazon api serializer configuration for employee_computer
"""

from rest_framework import serializers
from bangazon.api.models import *


class EmployeeComputerSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the employee_computer model database table into Python data types.

    We exclude no fields.

    Author: Zak Spence
    """

    class Meta:
        model = EmployeeComputer
        exclude = ()