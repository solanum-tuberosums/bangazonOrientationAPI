"""
bangazon api custom command to build database
"""

from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import makemigrations


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
        management.call_command('loaddata', 'department', 'computer', 'training_program',
            'customer', 'employee', 'payment_type', 'product_type', 'product',
            'order', 'order_product', 'employee_training', 'employee_computer')