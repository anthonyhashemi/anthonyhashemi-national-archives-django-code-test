# Getting Started

## Pre-requisites
- `python 3`
- `poetry 1.2.2`

## Install dependencies
- `poetry install`

## Running the `import_tna_record_data` management command
- `poetry run python manage.py import_tna_record_data <id>` where `id` is the id of an entry in TNA's records database.

## Running the API
- `poetry run python manage.py runserver`
- Given a valid `id` that you have imported data for using the management command above, you should be able to make a GET request to `http://127.0.0.1:8000/record/<id>/` with this `id` and should see some data that represents this record.
- The response will vary depending on whether the corresponding record in the database, using the following in order if available:
    - `title`
    - `scopeContent.description`
    - `citableReference`
- If these are all `null`, then the message "not sufficient information" will be displayed.
- If you have yet to import the data for a given `id`, then the message "no record found" will be displayed.

## Running tests
- `poetry run pytest .`

## Assumptions
- IDs in the TNA's record database are strings of at most 36 characters in length - some of which are GUIDs but not necessarily so (initially had started with this assumption but corrected this after double checking some ids using the search functionality and the titanic example)