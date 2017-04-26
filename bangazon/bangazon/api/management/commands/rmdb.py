import os
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Deletes the local copies of the db.sqlite3 file and the bangazon/api/migrations/ directory.'

    def handle(self, *args, **options):
        db_deleted = "FALSE"

        try:
            os.system("rm -rf bangazon/api/migrations/")
            migrations_deleted = "TRUE "
        except:
            migrations_deleted = "FALSE"

        if os.path.isfile('db.sqlite3'):
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
        else:
            db_deleted = "FALSE"
            self.stdout.write("\n \n      BANGAZON: Database does not exist, so it could not be deleted.\n ")

