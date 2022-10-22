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
        title = data["title"]
        if title:
            message = title
        else:
            scope_content_description = data["scopeContent"]["description"]
            if scope_content_description:
                message = scope_content_description
    return HttpResponse(message, content_type="text/plain")
