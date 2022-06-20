from django.utils import timezone
from django.db import models
from django import forms
TARGETS = [
    ("I", "Individual"),
    ("S", "School"),
    ("PB", "Public Building"),
    ("O", "Other")
]
# Create your models here.
class InvolvedTech(models.Model):
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description
class ReportModel(models.Model):
    eventname = models.CharField(max_length=100)
    date = models.CharField(max_length=100) # MAKE THIS INTO A DATE FIELD
    target = models.CharField(max_length=100, choices=TARGETS)
    techinvolved = models.ManyToManyField(InvolvedTech)
    description = models.CharField(max_length=2000, default="N/A")
    mainlink = models.CharField(max_length=2000, default="N/A")
    targetother = models.CharField(max_length=200, default="N/A") # Figure out how to only create this if other is selected
    def __str__(self):
        return self.eventname
    techinvolved.verbose_name = "Tech Involved"
    eventname.verbose_name = "Event Name"
    mainlink.verbose_name = "Main Link"
    targetother.verbose_name = "Target Other"
