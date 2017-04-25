"""
bangazon api view configuration for training program
"""

from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *


class TrainingProgramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows training program data to be viewed or edited

    Author: Adam Myers
    """
    
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer