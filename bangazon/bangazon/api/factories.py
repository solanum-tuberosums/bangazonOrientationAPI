import factory
from bangazon.api.models import *

class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department
    name = factory.Sequence(lambda n: "Department %03d" % n)
    budget = factory.Sequence(lambda n: "{}".format(n))

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    date_created = "2012-04-25"