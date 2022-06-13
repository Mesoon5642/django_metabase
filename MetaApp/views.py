from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import ReportForm
from .models import ReportModel

# Create your views here.

def submit_report(request):
    print("lmfao")
    reportform = ReportForm(request.POST)
    if reportform.is_valid():
        reportmodel = ReportModel.objects.create()
        print("lmfao")
        reportmodel.date = reportform.cleaned_data.get("date")
        reportmodel.time = reportform.cleaned_data.get("time")
        reportmodel.crimecategory = reportform.cleaned_data.get("crimecategory")
        reportmodel.platform = reportform.cleaned_data.get("platform")
        reportmodel.description = reportform.cleaned_data.get("description")
        reportmodel.medialinks = reportform.cleaned_data.get("medialinks")
        reportmodel.govreport = reportform.cleaned_data.get("govreport")
        reportmodel.save()
        return HttpResponseRedirect("thanks.html")
    print("false")
    return render(request, "submit_report.html", {"report_form":reportform})
