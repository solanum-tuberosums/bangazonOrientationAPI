from rest_framework import serializers
from bangazon.api.models.model_department import Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    """
    This class converts the department model into native Python datatypes.

    We exclude no fields.

    Author: Jeremy Bakker
    """

    class Meta:
        model = Department
        exclude = ()