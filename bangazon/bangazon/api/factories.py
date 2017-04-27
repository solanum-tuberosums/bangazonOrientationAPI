import factory
from bangazon.api.models import *
from faker import Faker
fake = Faker()

class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department
    name = fake.company()
    budget = fake.random_int()

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
    first_name = fake.first_name()
    last_name = fake.last_name()
    date_created = fake.date()

class ComputerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Computer
    serial_number = fake.ean13()
    date_purchased = fake.date()
    date_decommissioned = None

class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType
    label = fake.word()

class TrainingProgramFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TrainingProgram
    name = fake.bs()
    start_date = fake.date()
    end_date = fake.date()
    max_enrollment = fake.random_int(min=10, max=50)

class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee
    first_name = fake.first_name()
    last_name = fake.last_name()
    is_supervisor = 0
    department_id = factory.Iterator(Department.objects.all())

class SupervisorFactory(EmployeeFactory):
    is_supervisor = 1

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    price = fake.random_int()
    title = fake.word()
    description = fake.text()
    product_type = factory.Iterator(ProductType.objects.all())
    customer = factory.Iterator(Customer.objects.all())

class PaymentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PaymentType
    account_label = fake.word()
    account_type = fake.credit_card_provider()
    account_number = fake.credit_card_number()
    customer_id = factory.Iterator(Customer.objects.all())

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order
    payment_type_id = None
    order_date = fake.date()
    customer_id = factory.Iterator(Customer.objects.all())

class OrderProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderProduct
    product_id = factory.Iterator(Product.objects.all())
    order_id = factory.Iterator(Order.objects.all())

class EmployeeComputerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmployeeComputer
    date_assigned = fake.date()
    employee_id = factory.Iterator(Employee.objects.all())
    computer_id = factory.Iterator(Computer.objects.all())

class EmployeeTrainingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmployeeTraining
    training_id = factory.Iterator(TrainingProgram.objects.all())
    employee_id = factory.Iterator(Employee.objects.all())










