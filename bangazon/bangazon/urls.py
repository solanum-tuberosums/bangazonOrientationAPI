from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers


from bangazon.api.views import *

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'producttype', ProductTypeViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'order', OrderViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
