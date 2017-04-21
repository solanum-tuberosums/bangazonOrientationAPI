from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bangazon.api.models.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')