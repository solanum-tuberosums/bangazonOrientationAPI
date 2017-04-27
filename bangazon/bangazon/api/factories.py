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
    serial_number = factory.Faker('uuid4')
    date_purchased = factory.Faker('date')
    date_decommissioned = None