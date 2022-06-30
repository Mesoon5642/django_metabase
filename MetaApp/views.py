from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import RequestContext
import json
from httplib2 import Http
from .forms import CreateAccountForm, EvidenceForm, RelevantLocationForm, ReportForm, LoginForm, SuspectForm
from .models import AdminUserModel, ReportModel
import random

# Create your views here.

def submit_report(request):
    if (request.COOKIES["LOGGED_USERNAME"] == ""):
        return HttpResponseRedirect(reverse("MetaApp:login"))
    else:
        reportform = ReportForm(request.POST)
        if reportform.is_valid() and ReportModel.objects.filter(eventname=reportform.cleaned_data.get("eventname")).count() < 1:
            reportmodel = ReportModel.objects.create()
            reportmodel.eventname = reportform.cleaned_data.get("eventname")
            reportmodel.date = reportform.cleaned_data.get("date")
            reportmodel.target = reportform.cleaned_data.get("target")
            reportmodel.targetother = reportform.cleaned_data.get("targetother")
            reportmodel.techinvolved.set(reportform.cleaned_data.get("techinvolved"))
            reportmodel.description = reportform.cleaned_data.get("description")
            reportmodel.mainlink = reportform.cleaned_data.get("mainlink")
            reportmodel.author = str(request.COOKIES["LOGGED_REALNAME"])
            reportmodel.readabletech = reportmodel.readtech()
            if (reportform.cleaned_data.get("cryptoamount")):
                reportmodel.cryptoamount = reportform.cleaned_data.get("cryptoamount")
            print(random.randint(1000000, 9999999))
            tempid = random.randint(1000000, 9999999)
            print(tempid)
            while (ReportModel.objects.filter(reportid=tempid).count() > 0):
                tempid = random.randint(1000000, 9999999)
            print(tempid)
            reportmodel.reportid = tempid
            reportmodel.save()
            return render (request, "thanks.html")
    print(reportform.errors)
    return render(request, "submit_report.html", {"report_form":reportform})
def thanks(request):
    return render (request, "thanks.html")
def index(request):
    return render (request, "index.html")
def viewdata(request):
    return render(request, "viewdata.html", {"tech_data":ReportModel.techcount(), "target_data":ReportModel.targetcount()})
def login(request):
    loginform = LoginForm(request.POST)
    if loginform.is_valid():
        if (AdminUserModel.objects.filter(username=loginform.cleaned_data.get("username")).count() > 0) and (AdminUserModel.objects.get(username=loginform.cleaned_data.get("username")).verified):
            response = HttpResponseRedirect(reverse("MetaApp:submit_report"))
            response.set_cookie("LOGGED_USERNAME", loginform.cleaned_data.get("username"), 86400)
            response.set_cookie("LOGGED_REALNAME", AdminUserModel.objects.get(username=loginform.cleaned_data.get("username")).realname, 86400)
            return response
    return render(request, "login.html", {"login_form":loginform})
def create(request):
    createform = CreateAccountForm(request.POST)
    print("yes")
    if createform.is_valid() and (createform.cleaned_data.get("password") == createform.cleaned_data.get("confirmpassword")) and (AdminUserModel.objects.filter(username=createform.cleaned_data.get("username")).count() < 1):
        usermodel = AdminUserModel.objects.create()
        usermodel.realname = createform.cleaned_data.get("realname")
        usermodel.username = createform.cleaned_data.get("username")
        usermodel.password = createform.cleaned_data.get("password")
        usermodel.verified = False
        usermodel.save()
        return render (request, "thanks.html")
    return render (request, "create_account.html", {"create_form":createform})
def viewreports(request):
    return render (request, "viewreports.html", {"reportobjects":ReportModel.objects.all()})
def viewdetail(request, rid):
    return render (request, "viewdetail.html", {"report":ReportModel.objects.get(reportid=rid)})
def addevidence(request, rid):
    if (request.COOKIES["LOGGED_USERNAME"] == ""):
        return HttpResponseRedirect(reverse("MetaApp:login"))
    else:
        evidenceform = EvidenceForm(request.POST)
    return render (request, "addevidence.html", {"report":ReportModel.objects.get(reportid=rid), "evidence_form":evidenceform})
def addsuspect(request, rid):
    if (request.COOKIES["LOGGED_USERNAME"] == ""):
        return HttpResponseRedirect(reverse("MetaApp:login"))
    else:
        suspectform = SuspectForm(request.POST)
    return render (request, "addsuspect.html", {"report":ReportModel.objects.get(reportid=rid), "suspect_form":suspectform})
def addlocation(request, rid):
    if (request.COOKIES["LOGGED_USERNAME"] == ""):
        return HttpResponseRedirect(reverse("MetaApp:login"))
    else:
        locationform = RelevantLocationForm(request.POST)
    return render (request, "addlocation.html", {"report":ReportModel.objects.get(reportid=rid), "location_form":locationform})