from django.db import models


class Record(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    data = models.JSONField()
