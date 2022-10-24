"""Models for the records app"""

from django.db import models


class Record(models.Model):
    """Model holding data for TNA Record entries"""
    id = models.CharField(max_length=36, primary_key=True)
    data = models.JSONField()
