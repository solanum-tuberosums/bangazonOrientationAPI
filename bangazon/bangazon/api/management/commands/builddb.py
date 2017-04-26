"""
bangazon api custom command to build database
"""

from django.core.management.base import BaseCommand, CommandError
import os


class Command(BaseCommand):
    """
    Defines what the 'builddb' command should do
    and what the '--help' option will display to the user.

    Author: Blaise Roberts
    """

    help = 'Builds and populates your database tables.'

    def handle(self, *args, **options):
        os.system("python manage.py makemigrations api")
        os.system("python manage.py migrate")
        os.system("python manage.py loaddata department")
        os.system("python manage.py loaddata computer")
        os.system("python manage.py loaddata training_program")
        os.system("python manage.py loaddata customer")
        os.system("python manage.py loaddata product_type")
        os.system("python manage.py loaddata employee")
        os.system("python manage.py loaddata payment_type")
        os.system("python manage.py loaddata product")
        os.system("python manage.py loaddata order")
        os.system("python manage.py loaddata order_product")
        os.system("python manage.py loaddata employee_training")
        os.system("python manage.py loaddata employee_computer")
        self.stdout.write("The database has been loaded successfully.")
