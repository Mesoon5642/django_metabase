from pyexpat import model
from django.db import models
TARGETS = [
    ("Individual", "Individual"),
    ("School", "School"),
    ("Public Building", "Public Building"),
    ("Other", "Other")
]
# Create your models here.
class InvolvedTech(models.Model):
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description
class RelevantLocationModel(models.Model):
    name =  models.CharField(max_length=300)
    description = models.CharField(max_length=2000)
    def __str__(self):
        return self.name
class EvidenceModel(models.Model):
    name = models.CharField(max_length=200, default="")
    datefound = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, default="")
    def __str__(self):
        return self.name
class SuspectModel(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=2000, default="")
    age = models.IntegerField(default=18)
    evidence = models.ManyToManyField(EvidenceModel)
    guilty = models.BooleanField(default=False)
    def __str__(self):
        return self.name
class ReportModel(models.Model):
    eventname = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    target = models.CharField(max_length=100, choices=TARGETS)
    techinvolved = models.ManyToManyField(InvolvedTech)
    description = models.CharField(max_length=2000, default="N/A")
    mainlink = models.CharField(max_length=2000, default="N/A")
    targetother = models.CharField(max_length=200, default="N/A")
    author = models.CharField(max_length=200, default="Superuser")
    relevantlocations = models.ManyToManyField(RelevantLocationModel)
    evidence = models.ManyToManyField(EvidenceModel)
    suspects = models.ManyToManyField(SuspectModel)
    closed = models.BooleanField(default=False)
    cryptoamount = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    def __str__(self):
        return self.eventname
    def techcount():
        techlist = []
        for thing in InvolvedTech.objects.all():
            techlist.append(ReportModel.objects.filter(techinvolved=thing).count())
        return techlist
    def targetcount():
        targetlist = []
        for thing in TARGETS:
            targetlist.append(ReportModel.objects.filter(target=thing[0]).count())
        return targetlist
    def readtech(self):
        techlist = ""
        for thing in self.techinvolved.all():
            techlist += (thing.__str__() + ",")
        techlist = techlist[0:(len(techlist) - 1)]
        return techlist
    readabletech = models.CharField(max_length=1000)
    techinvolved.verbose_name = "Tech Involved"
    eventname.verbose_name = "Event Name"
    mainlink.verbose_name = "Main Link"
    targetother.verbose_name = "Other Target"
    cryptoamount.verbose_name = "Crypto Amount"
class AdminUserModel(models.Model): #Verify input
    realname = models.CharField(max_length=200)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    realname.verbose_name = "Real Name"