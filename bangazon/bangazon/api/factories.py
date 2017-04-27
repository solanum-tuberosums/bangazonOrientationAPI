import factory
from bangazon.api.models import *

class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department
    name = factory.Faker('company')
    budget = factory.Faker('random_int', min=1, max=100)

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    date_created = factory.Faker('date')

class ComputerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Computer
    serial_number = factory.Faker('ean13')
    date_purchased = factory.Faker('date')
    date_decommissioned = None

class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType
    label = factory.Faker('word')

class TrainingProgramFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TrainingProgram
    name = factory.Faker('bs')
    start_date = factory.Faker('date')
    end_date = factory.Faker('date')
    max_enrollment = factory.Faker('random_int', min=10, max=100)

class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_supervisor = 0
    department_id = factory.Iterator(Department.objects.all())

class SupervisorFactory(EmployeeFactory):
    is_supervisor = 1

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    price = factory.Faker('random_int')
    title = factory.Faker('word')
    description = factory.Faker('text')
    product_type = factory.Iterator(ProductType.objects.all())
    customer = factory.Iterator(Customer.objects.all())

class PaymentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PaymentType
    account_label = factory.Faker('word')
    account_type = factory.Faker('credit_card_provider')
    account_number = factory.Faker('credit_card_number')
    customer_id = factory.Iterator(Customer.objects.all())

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order
    payment_type_id = None
    order_date = factory.Faker('date')
    customer_id = factory.Iterator(Customer.objects.all())

class OrderProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderProduct
    product_id = factory.Iterator(Product.objects.all())
    order_id = factory.Iterator(Order.objects.all())

class EmployeeComputerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmployeeComputer
    date_assigned = factory.Faker('date')
    employee_id = factory.Iterator(Employee.objects.all())
    computer_id = factory.Iterator(Computer.objects.all())

class EmployeeTrainingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmployeeTraining
    training_id = factory.Iterator(TrainingProgram.objects.all())
    employee_id = factory.Iterator(Employee.objects.all())