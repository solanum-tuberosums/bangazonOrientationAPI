from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):
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
        self.stdout.write("Potato DB has been successfully loaded, bro!")