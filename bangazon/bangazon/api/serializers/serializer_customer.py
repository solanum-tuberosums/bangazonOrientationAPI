from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bangazon.api.models.model_customer import Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    """
    This class converts the customer model into native Python datatypes.

    We exclude no fields.

    Author: Zak Spence
    """

    class Meta:
        model = Customer
        exclude = ()
