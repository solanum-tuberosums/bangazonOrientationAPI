"""
bangazon api view configuration for computer
"""

from rest_framework import viewsets
from bangazon.api.serializers.serializer_computer import ComputerSerializer
from bangazon.api.models.model_computer import Computer


class ComputerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computer data to be viewed or edited

    Author: Zak Spence
    """

    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
