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
        techlist = []
        jsondict = (
                {
                    "techinvolved": techlist
                }
        )
        jsondat = json.dumps(jsondict, indent=4) #FIX THE LINE BELOW TO NOT WORK LIKE THAT!!!!!
        with open("/home/mesoon/Desktop/Metaverse_Crime_Database/MetaData/MetaApp/static/MetaApp/lastform.json", "w") as outfile:
            outfile.write(jsondat)
        return render (request, "thanks.html")
    return render(request, "submit_report.html", {"report_form":reportform})
def thanks(request):
    return render (request, "thanks.html")
def index(request):
    return render (request, "index.html")