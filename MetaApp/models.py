from django.utils import timezone
from django.db import models
from django import forms

CRIME_CATEGORIES = [
    ("AS", "Assault"),
    ("SV", "Sexual Violence")
]
# Create your models here.
class ReportModel(models.Model):
    date = models.DateField()
    time = models.TimeField()
    crimecategory = models.CharField("Crime Category", max_length=100, choices=CRIME_CATEGORIES)
    platform = models.CharField(max_length=100, default="N/A")
    description = models.CharField(max_length=2000, default="N/A")
    medialinks = models.CharField(max_length=2000, default="N/A") # Figure out a way to do this to add each link individually
    govreport = models.CharField(max_length=300, default="N/A")
