"""
bangazon api serializer configuration for department
"""

from rest_framework import serializers
from bangazon.api.models import *


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the department model database table into Python data types.

    We exclude no fields.

    Author: Jeremy Bakker
    """

    class Meta:
        model = Department
        exclude = ()