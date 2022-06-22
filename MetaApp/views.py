from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import json
from httplib2 import Http
from .forms import ReportForm
from .models import InvolvedTech, ReportModel

# Create your views here.

def submit_report(request):
    reportform = ReportForm(request.POST)
    if reportform.is_valid():
        reportmodel = ReportModel.objects.create()
        reportmodel.eventname = reportform.cleaned_data.get("eventname")
        reportmodel.date = reportform.cleaned_data.get("date")
        reportmodel.target = reportform.cleaned_data.get("target")
        reportmodel.techinvolved.set(reportform.cleaned_data.get("techinvolved"))
        reportmodel.description = reportform.cleaned_data.get("description")
        reportmodel.mainlink = reportform.cleaned_data.get("mainlink")
        reportmodel.save()
        return render (request, "thanks.html")
    return render(request, "submit_report.html", {"report_form":reportform})
def thanks(request):
    return render (request, "thanks.html")
def index(request):
    return render (request, "index.html", {"tech_data":ReportModel.techcount()})