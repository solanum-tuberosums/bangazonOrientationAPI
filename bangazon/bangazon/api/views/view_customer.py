from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from bangazon.api.serializers import serializer_customer
from bangazon.api.models import model_customer


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.

    Author: Zak Spence
    """
    queryset = model_customer.Customer.objects.all()
    serializer_class = serializer_customer.CustomerSerializer
