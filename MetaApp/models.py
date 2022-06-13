from django.db import models
from django import forms

# Create your models here.
class ReportModel(models.Model):
    date = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    crimecategory = models.CharField(max_length=100, default="N/A")
    platform = models.CharField(max_length=100, default="N/A")
    description = models.CharField(max_length=2000, default="N/A")
    medialinks = models.CharField(max_length=2000, default="N/A") # Figure out a way to do this to add each link individually
    govreport = models.CharField(max_length=300, default="N/A")
