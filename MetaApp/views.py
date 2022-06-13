from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import ReportForm
from .models import ReportModel

# Create your views here.

def submit_report(request):
    reportform = ReportForm(request.POST)
    if reportform.is_valid():
        reportmodel = ReportModel.objects.create()
        reportmodel.date = reportform.cleaned_data.get("date")
        reportmodel.time = reportform.cleaned_data.get("time")
        reportmodel.crimecategory = reportform.cleaned_data.get("crimecategory")
        reportmodel.platform = reportform.cleaned_data.get("platform")
        reportmodel.description = reportform.cleaned_data.get("description")
        reportmodel.medialinks = reportform.cleaned_data.get("medialinks")
        reportmodel.govreport = reportform.cleaned_data.get("govreport")
        reportmodel.save()
        return HttpResponseRedirect(reverse("thanks"))
    return render(request, "submit_report.html", {"report_form":reportform})
def thanks(request):
    return render (request, "thanks.html")