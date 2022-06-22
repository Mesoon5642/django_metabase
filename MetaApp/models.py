from django.db import models
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
    date = models.CharField(max_length=100)
    target = models.CharField(max_length=100, choices=TARGETS)
    techinvolved = models.ManyToManyField(InvolvedTech)
    description = models.CharField(max_length=2000, default="N/A")
    mainlink = models.CharField(max_length=2000, default="N/A")
    targetother = models.CharField(max_length=200, default="N/A")
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
    techinvolved.verbose_name = "Tech Involved"
    eventname.verbose_name = "Event Name"
    mainlink.verbose_name = "Main Link"
    targetother.verbose_name = "Other Target"
    cryptoamount.verbose_name = "Crypto Amount"
