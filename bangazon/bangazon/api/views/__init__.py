from bangazon.api.views.view_customer import CustomerViewSet
from bangazon.api.views.view_product import ProductViewSet
from bangazon.api.views.view_product_type import ProductTypeViewSet
from bangazon.api.views.view_order import OrderViewSet
from bangazon.api.views.view_training_program import TrainingProgramViewSet
from bangazon.api.views.view_payment_type import PaymentTypeViewSet

__all__ = ['ProductTypeViewSet',
           'ProductViewSet', 'CustomerViewSet','OrderViewSet', 'TrainingProgramViewSet', 'PaymentTypeViewSet']
