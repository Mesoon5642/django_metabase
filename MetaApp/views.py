from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import ReportForm
from .models import TECH_INVOLVED, ReportModel

# Create your views here.

def submit_report(request):
    reportform = ReportForm(request.POST)
    print(reportform.data)
    reportform.fields["techinvolved"]
    if reportform.is_valid():
        print("hello")
        reportmodel = ReportModel.objects.create(name="bruh")
        reportmodel.eventname = reportform.cleaned_data.get("eventname")
        reportmodel.date = reportform.cleaned_data.get("date")
        reportmodel.target = reportform.cleaned_data.get("target")
        reportmodel.techinvolved.set(reportform.cleaned_data.get("techinvolved"))
        reportmodel.description = reportform.cleaned_data.get("description")
        reportmodel.mainlink = reportform.cleaned_data.get("mainlink")
        reportmodel.save()
        return HttpResponseRedirect(reverse("thanks"))
    else:
        print(reportform.errors)
    return render(request, "submit_report.html", {"report_form":reportform})
def thanks(request):
    return render (request, "thanks.html")