# Generated by Django 4.1.2 on 2022-10-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
            fields=[
                (
                    "id",
                    models.CharField(max_length=36, primary_key=True, serialize=False),
                ),
                ("data", models.JSONField()),
            ],
        ),
    ]
