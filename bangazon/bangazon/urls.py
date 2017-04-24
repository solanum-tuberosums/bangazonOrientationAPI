from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from bangazon.api.views import views

router = routers.DefaultRouter()

router.register(r'products', views.ProductViewSet)
router.register(r'producttype', views.ProductTypeViewSet)
router.register(r'customers', views.CustomerViewSet)





urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
