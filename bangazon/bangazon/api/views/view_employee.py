"""
bangazon api view configuration for employee
"""

from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employee data to be viewed or edited

    Author: Adam Myers
    """
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer