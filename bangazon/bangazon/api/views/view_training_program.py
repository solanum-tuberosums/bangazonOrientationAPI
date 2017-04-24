"""
bangazon api view Configuration for training program
"""

from rest_framework import viewsets
from bangazon.api.serializers.serializer_training_program import *
from bangazon.api.models.model_training_program import *

class TrainingProgramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view all in training program table.

    Author:
        Adam Myers
    """
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer