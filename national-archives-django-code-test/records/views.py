from django.core.exceptions import ValidationError
from django.http import HttpResponse

from records.models import Record

def get_record(request, guid):
    try:
        record = Record.objects.get(guid=guid)
    except (Record.DoesNotExist, ValidationError):
        message = "no record found"
    else:
        data = record.data
        message = data["title"]
    return HttpResponse(message,content_type="text/plain")
