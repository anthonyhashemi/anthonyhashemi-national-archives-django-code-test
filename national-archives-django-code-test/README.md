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
