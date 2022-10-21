import requests
from django.core.management.base import BaseCommand

from records.models import Record


class Command(BaseCommand):
    help = "Imports record data from the tna API"

    def add_arguments(self, parser):
        parser.add_argument("guid", type=str)

    def handle(self, *args, **kwargs):
        guid = kwargs["guid"]
        if Record.objects.filter(guid=guid).exists():
            self.stdout.write(
                self.style.WARNING(
                    'Record for guid "%s" alredy exists in the database.' % guid
                )
            )
        else:
            response = requests.get(
                f"http://discovery.nationalarchives.gov.uk/API/records/v1/details/{guid}"
            )
            data = response.json()
            Record.objects.create(guid=guid, data=data)
            self.stdout.write(
                self.style.SUCCESS(
                    'Record for guid "%s" created in the database.' % guid
                )
            )
