from rest_framework import serializers
from bangazon.api.models.model_product_type import *

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        exclude = ()