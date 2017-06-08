from bangazon.api.views.view_customer import CustomerViewSet
from bangazon.api.views.view_product import ProductViewSet
from bangazon.api.views.view_product_type import ProductTypeViewSet
from bangazon.api.views.view_order import OrderViewSet
from bangazon.api.views.view_training_program import TrainingProgramViewSet
from bangazon.api.views.view_payment_type import PaymentTypeViewSet
from bangazon.api.views.view_department import DepartmentViewSet
from bangazon.api.views.view_computer import ComputerViewSet
from bangazon.api.views.view_employee import EmployeeViewSet
from bangazon.api.views.view_customer_support_ticket import CustomerSupportTicketViewSet
from bangazon.api.views.get_order_view import get_order
from bangazon.api.views.register_view import register_user
from bangazon.api.views.user_logout_view import user_logout

__all__ = [
    'ProductTypeViewSet',
    'ProductViewSet',
    'CustomerViewSet',
    'OrderViewSet',
    'TrainingProgramViewSet',
    'PaymentTypeViewSet',
    'DepartmentViewSet',
    'EmployeeViewSet',
    'ComputerViewSet',
    'CustomerSupportTicketViewSet',
    'get_order',
    'register_user',
    'user_logout',
    ]
