"Tests for the import_tna_record_data management command"

import json

from django.core.management import call_command
from django.test import TestCase

from records.models import Record


class ImportTNARecordData(TestCase):
    def test_command_output(self):
        """
        Given a valid ID
        When import_tna_record_data is called with this parameter
        Then a new entry is created in the `Record` model
        for this ID
        """
        id = "a147aa58-38c5-45fb-a340-4a348efa01e6"
        call_command("import_tna_record_data", str(id))

        record = Record.objects.get(id=id)
        with open("records/tests/record_data.json") as json_file:
            expected_data = json.load(json_file)
        self.assertEqual(record.data, expected_data)
