from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from bangazon.api.views import view_payment_type
from bangazon.api.views import view_customer
from bangazon.api.views import view_product_type


router = routers.DefaultRouter()
router.register(r'payment_types', view_payment_type.PaymentTypeViewSet)
router.register(r'customers', view_customer.CustomerViewSet)
router.register(r'producttype', view_product_type.ProductTypeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
