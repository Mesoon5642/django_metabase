import csv
from pyexpat import model
from django.contrib import admin
from django.http import HttpResponse

from .models import EvidenceModel, RelevantLocationModel, ReportModel, InvolvedTech, AdminUserModel, SuspectModel

# Register your models here.



class ReportModelAdmin(admin.ModelAdmin):
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
    list_filter = ["target", "techinvolved", "author"]
    list_display = ("eventname", "date", "author", "reportid")
    ordering = ["date"]
    fieldsets = (
        ("Main", {"fields": ["eventname", "date", "target", "techinvolved", "description", "mainlink", "closed", "reportid", "author"]}),
        ("Extras", {"fields": ["targetother", "cryptoamount"]}),
        ("Related Data", {"fields": ["relevantlocations", "suspects", "evidence"]})
    )
    
    actions = ["export_as_csv"]
    export_as_csv.short_description = "Export Selected"
class AdminUserModelAdmin(admin.ModelAdmin):
    def verify(self, request, queryset):
        for obj in queryset:
            obj.verified = True
            obj.save()
    list_display = ("realname", "username", "verified")
    list_filter = ["verified"]
    ordering = ["realname"]
    actions = ["verify"]
admin.site.register(ReportModel, ReportModelAdmin)
admin.site.register(InvolvedTech)
admin.site.register(RelevantLocationModel)
admin.site.register(EvidenceModel)
admin.site.register(SuspectModel)
admin.site.register(AdminUserModel, AdminUserModelAdmin)
