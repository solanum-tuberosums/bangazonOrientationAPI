from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from bangazon.api.serializers import serializer_customer
from bangazon.api.models import model_customer


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = User.objects.all().order_by('last_name')
    serializer_class = serializer_customer.CustomerSerializer
