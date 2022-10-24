"""Views for the records app"""

from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse

from records.models import Record


def get_record(request: HttpRequest, id: int) -> HttpResponse:
    """
    Detail view which returns a signifier of a Record for the given id.
    
    The response will vary depending on whether the corresponding record
    in the database, using the following in order if available:
    - `title`
    - `scopeContent.description`
    - `citableReference`
    
    If these are all `null`, then the message "not sufficient information"
    will be displayed.
    If you have yet to import the data for a given `id`, then the
    message "no record found" will be 

    Args:
        request (HttpRequest): http request object
        id (int): id of Request object to fetch

    Returns:
        (HttpResponse) http response
    """
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
