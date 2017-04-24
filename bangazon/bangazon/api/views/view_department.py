"""
bangazon api view configuration for order
"""

from django.shortcuts import render
from rest_framework import viewsets
from bangazon.api.serializers.serializer_department import *
from bangazon.api.models.model_department import *


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ALL orders to be viewed or edited.

    Author: Jeremy Bakker
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer