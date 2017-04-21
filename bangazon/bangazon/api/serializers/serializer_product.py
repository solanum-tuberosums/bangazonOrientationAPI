from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bangazon.api.models.model_product import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Product Serializer
    - Author: Will Sims
    - Purpose: Converts database tables into Python data types to be rendered in JSON/XML
    - Excluded no fields.
    """
    class Meta:
        model = Product
        fields = ['url', 'Price', 'Title', 'Description']


        #'ProductTypeId', 'CustomerId']

