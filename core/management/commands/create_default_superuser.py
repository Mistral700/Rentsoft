from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = 'Creates a default superuser if it does not exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not (email and password):
            self.stdout.write(self.style.WARNING("Superuser credentials not set. Skipping."))
            return

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{email}' created."))
        else:
            self.stdout.write(self.style.NOTICE(f"Superuser '{email}' already exists."))
