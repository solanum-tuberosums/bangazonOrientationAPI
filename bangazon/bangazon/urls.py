from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from bangazon.api.views import view_payment_type
from bangazon.api.views import view_customer
from bangazon.api.views import view_product_type
from bangazon.api.views import view_order
from bangazon.api.views.view_department import *
from bangazon.api.views import *



router = routers.DefaultRouter()
router.register(r'payment_types', view_payment_type.PaymentTypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'producttype', ProductTypeViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'order', OrderViewSet)
router.register(r'department', DepartmentViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
