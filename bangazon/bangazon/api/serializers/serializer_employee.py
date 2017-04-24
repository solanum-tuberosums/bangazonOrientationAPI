"""
bangazon api serializer Configuration for employee
"""

from rest_framework import serializers
from bangazon.api.models.model_employee import *

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts database tables into Python data types

    We exclude no fields.

    Author:
        Adam Myers
    """
    class Meta:
        model = Employee
        exclude = ()