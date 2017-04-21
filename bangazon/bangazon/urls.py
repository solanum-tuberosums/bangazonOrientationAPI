from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from bangazon.api.views import view_customer

router = routers.DefaultRouter()
router.register(r'customers', view_customer.CustomerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
