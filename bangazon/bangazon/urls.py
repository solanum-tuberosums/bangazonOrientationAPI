from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from bangazon.api.views import *
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register(r'payment_types', PaymentTypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_type', ProductTypeViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'order', OrderViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'training_program', TrainingProgramViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'computers', ComputerViewSet)
router.register(r'customer_support_ticket', CustomerSupportTicketViewSet)

urlpatterns = [
    url(r'^get_order$', get_order, name='get_order'),
    url(r'^logout$', user_logout, name='logout'),
    url(r'^register$', register_user, name='register'),
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

