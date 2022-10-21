from django.db import models


class Record(models.Model):
    guid = models.UUIDField(unique=True)
    data = models.JSONField()
