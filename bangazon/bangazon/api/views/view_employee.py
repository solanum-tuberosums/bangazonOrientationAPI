"""
bangazon api view Configuration for employee
"""

from rest_framework import viewsets
from bangazon.api.serializers.serializer_employee import *
from bangazon.api.models.model_employee import *


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view all in employee table.

    Author:
    	Adam Myers
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer