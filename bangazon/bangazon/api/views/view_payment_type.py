from rest_framework import viewsets
from bangazon.api.serializers.serializer_payment_type import *
from bangazon.api.models.model_payment_type import *

class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer