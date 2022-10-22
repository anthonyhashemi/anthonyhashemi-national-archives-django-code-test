import requests
from django.core.management.base import BaseCommand

from records.models import Record


class Command(BaseCommand):
    help = "Imports record data from the tna API"

    def add_arguments(self, parser):
        parser.add_argument("id", type=str)

    def handle(self, *args, **kwargs):
        id = kwargs["id"]
        if Record.objects.filter(id=id).exists():
            self.stdout.write(
                self.style.WARNING(
                    'Record for id "%s" alredy exists in the database.' % id
                )
            )
        else:
            response = requests.get(
                f"http://discovery.nationalarchives.gov.uk/API/records/v1/details/{id}"
            )
            data = response.json()
            Record.objects.create(id=id, data=data)
            self.stdout.write(
                self.style.SUCCESS(
                    'Record for id "%s" created in the database.' % id
                )
            )
