"""
bangazon api custom command to build database
"""

from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import makemigrations
from bangazon.api.factories import *


class Command(BaseCommand):
    """
    Defines the command 'builddb', which is a shortcut for running
    all the necessary shell commands to generate our database's tables and
    load our fixtures to our database. These commands are, in order:
    1. python manage.py makemigrations api
    2. python manage.py migrate
    3. python manage.py loaddata <fixtures>

    Author: Jeremy Bakker
    """

    def handle(self, *args, **options):
        management.call_command('makemigrations', 'api')
        management.call_command('migrate')
        # management.call_command('loaddata', 'department', 'computer', 'training_program',
        #     'customer', 'employee', 'payment_type', 'product_type', 'product',
        #     'order', 'order_product', 'employee_training', 'employee_computer')
        DepartmentFactory.create_batch(size=10)
        CustomerFactory.create_batch(size=100)
        ComputerFactory.create_batch(size=100)
        TrainingProgramFactory.generate_batch('create', size=10)
        ProductTypeFactory.create_batch(size=10)
        EmployeeFactory.create_batch(size=100)
        SupervisorFactory.create_batch(size=10)
        ProductFactory.create_batch(size=50)
        PaymentTypeFactory.create_batch(size=100)
        OrderFactory.create_batch(size=100)
        OrderProductFactory.create_batch(size=100)
        EmployeeComputerFactory.create_batch(size=100)
        EmployeeTrainingFactory.create_batch(size=30)



