"""
bangazon api view configuration for product
"""

from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product data to be viewed or edited

    Author: Will Sims
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer