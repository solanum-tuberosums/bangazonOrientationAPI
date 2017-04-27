import factory
from bangazon.api.models import *

class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department
    name = factory.Faker('company')
    budget = factory.Faker('random_int')

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
    max_enrollment = factory.Faker('random_int')

class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_supervisor = 0
    department_id = factory.Iterator(Department.objects.all())





