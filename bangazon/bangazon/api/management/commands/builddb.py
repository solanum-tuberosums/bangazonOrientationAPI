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
        DepartmentFactory.create_batch(size=3)
        CustomerFactory.create_batch(size=10)
        ComputerFactory.create_batch(size=5)
        TrainingProgramFactory.create_batch(size=5)
        ProductTypeFactory.create_batch(size=5)
        EmployeeFactory.create_batch(size=100)