from django.core.exceptions import ValidationError
from django.http import HttpResponse

from records.models import Record


def get_record(request, id):
    try:
        record = Record.objects.get(id=id)
    except (Record.DoesNotExist, ValidationError):
        return HttpResponse("no record found", content_type="text/plain")
    data = record.data
    message = (
        data["title"]
        or data["scopeContent"]["description"]
        or data["citableReference"]
        or "not sufficient information"
    )
    return HttpResponse(message, content_type="text/plain")
