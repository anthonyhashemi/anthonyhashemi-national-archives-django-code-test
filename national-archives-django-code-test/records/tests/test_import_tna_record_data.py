import json

from django.core.management import call_command
from django.test import TestCase

from records.models import Record


class ImportTNARecordData(TestCase):
    def test_command_output(self):
        """
        Given a valid GUID
        When import_tna_record_data is called with this parameter
        Then a new entry is created in the `Record` model
        for this GUID
        """
        guid = "a147aa58-38c5-45fb-a340-4a348efa01e6"
        call_command("import_tna_record_data", str(guid))

        record = Record.objects.get(guid=guid)
        with open("records/tests/record_data.json") as json_file:
            expected_data = json.load(json_file)
        self.assertEqual(record.data, expected_data)
