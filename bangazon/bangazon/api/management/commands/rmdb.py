import os
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    """
    Command: 'rmdb'
    Purpose: to delete db.sqlite3 and the api/migrations/ directory. Our team used to
              manually delete this file and this directory so we wrote a custom command
              to simplify the process.
    Author: Will Sims
    """

    help = 'Deletes the local copies of the db.sqlite3 file and the bangazon/api/migrations/ directory.'

    def handle(self, *args, **options):

        try:
            os.system("rm -rf bangazon/api/migrations/")
        except:
            pass

        try:
            os.system("rm db.sqlite3")
        except:
            pass
