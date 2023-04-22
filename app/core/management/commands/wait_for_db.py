import time

from psycopg2 import OperationalError as PsyError

from django.db.utils import OperationalError as OpError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Waiting for Database')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OpError, PsyError):
                self.stdout.write('Database unavailable')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database connected successfully'))
