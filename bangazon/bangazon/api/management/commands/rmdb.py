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
        db_deleted = "FALSE"

        try:
            os.system("rm -rf bangazon/api/migrations/")
            migrations_deleted = "TRUE "
        except:
            migrations_deleted = "FALSE"

        try:
            os.system("rm db.sqlite3")
            db_deleted = "TRUE"
            self.stdout.write("""
             ----------------------------------------------
             -----------------  SUCCESS   -----------------
             --- ------------------------------------------
             ---                                        ---
             ---   - Migrations Deleted:        {}   ---
             ---   - Database Deleted:          {}    ---
             ---                                        ---
             ----------------------------------------------
             ----------------------------------------------
             """.format(migrations_deleted, db_deleted))
        except:
            db_deleted = "FALSE"
            self.stdout.write("\n \n      BANGAZON: Database does not exist, so it could not be deleted.\n ")



