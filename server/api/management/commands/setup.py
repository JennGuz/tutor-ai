from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import User, Organization


EMAIL = 'admin@localhost.com'
PASSWORD = 'p'
ORG_NAME = 'Default Organization'


class Command(BaseCommand):
    help = 'Creates the default superuser and organization'

    def handle(self, *args, **options):
        with transaction.atomic():
            if User.objects.filter(username=EMAIL).exists():
                self.stdout.write(self.style.WARNING('Superuser already exists, skipping setup.'))
                return

            user = User.objects.create_superuser(
                username=EMAIL,
                email=EMAIL,
                password=PASSWORD,
            )

            org = Organization.objects.create(
                name=ORG_NAME,
                description='Default organization',
                owner=user,
            )

            user.organization = org
            user.save()

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('Setup complete!'))
        self.stdout.write(f'  Email:        {EMAIL}')
        self.stdout.write(f'  Username:     {EMAIL}')
        self.stdout.write(f'  Password:     {PASSWORD}')
        self.stdout.write(f'  Organization: {ORG_NAME}')
        self.stdout.write('')
