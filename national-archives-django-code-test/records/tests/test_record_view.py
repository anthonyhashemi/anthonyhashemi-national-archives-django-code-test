import json
import pytest
from django.test import TestCase
from django.urls import reverse

from records.models import Record


class RecordTests(TestCase):
    def test_record_with_title(self):
        """
        Given a valid record ID is specified
        When the client is run
        And the returned record's `title` is not null
        Then the record's `title` should be displayed
        """
        guid = "a147aa58-38c5-45fb-a340-4a348efa01e6"
        with open("records/tests/record_data_with_title.json") as json_file:
            data = json.load(json_file)
        record_with_text = Record.objects.create(guid=guid, data=data)
        assert (
            self.client.get(reverse("record-detail", kwargs={"guid": record_with_text.guid})).content.decode()
            == record_with_text.data["title"]
        )

    def test_invalid_guid_returns_no_record_found(self):
        """
        Given an invalid record ID is specified
        When the client is run
        Then a message "no record found" should be displayed
        """
        guid = "blah"
        assert (
            self.client.get(reverse("record-detail", kwargs={"guid": guid})).content.decode()
            == "no record found"
        )
    
    def test_guid_with_no_record_returns_no_record_found(self):
        """
        Given an invalid record ID is specified
        When the client is run
        Then a message "no record found" should be displayed
        """
        guid = "a147aa58-38c5-45fb-a340-4a348efa01e6"
        assert (
            self.client.get(reverse("record-detail", kwargs={"guid": guid})).content.decode()
            == "no record found"
        )
