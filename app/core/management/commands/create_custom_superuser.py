"""
Command for creating custom superuser
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """
    Django command for creating custom superuser
    """

    def add_arguments(self, parser):
        """Takes arguments from console"""
        parser.add_argument('--email', type=str, required=True, help='Superuser email')
        parser.add_argument('--password', type=str, required=True, help='Superuser password')

    def handle(self, *args, **options):
        """Entrypoint for command"""
        email = options['email']
        password = options['password']

        user = get_user_model()
        user_with_same_email = user.objects.filter(email=email).first()

        if user_with_same_email and user_with_same_email.is_superuser:
            self.stdout.write(f"Superuser with email {email} already exists.")
        elif user_with_same_email and not user.is_superuser:
            self.stdout.write(f"A user with email {email} exists but is not a superuser.")
        else:
            user.objects.create_superuser(email=email, password=password)
            self.stdout.write(f"Superuser {email} created successfully.")
