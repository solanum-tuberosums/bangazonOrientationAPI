"""
bangazon api serializer configuration for customer
"""

from rest_framework import serializers
from bangazon.api.models import *


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the customer model database table (for non-admins)  into Python data types.

    We excluded the 'date_created' field
    We included:
    	- url
    	- first_name
    	- last_name

    Author: Zak Spence
    """

    class Meta:
        model = Customer
        fields = ('url', 'first_name', 'last_name')

class AdminCustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the customer model database table (for admins)  into Python data types.

    We exclude no fields.

    Author: Will Sims
    """
    class Meta:
        model = Customer
        exclude = ()
