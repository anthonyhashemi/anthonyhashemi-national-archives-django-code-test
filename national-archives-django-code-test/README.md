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

## Running tests
- `poetry run pytest .`

## Assumptions
- IDs in the TNA's record database are strings of at most 36 characters in length - some of which are GUIDs but not necessarily so (initially had started with this assumption but corrected this after double checking some ids using the search functionality and the titanic example)