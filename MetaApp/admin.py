import csv
from django.contrib import admin
from django.http import HttpResponse

from .models import ReportModel, InvolvedTech

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
    list_filter = ["target", "techinvolved"]
    list_display = ("eventname", "date", "mainlink")
    ordering = ["date"]
    fieldsets = (
        ("Main", {"fields": ["eventname", "date", "target", "techinvolved", "description", "mainlink"]}),
        ("Extras", {"fields": ["targetother", "cryptoamount"]})
    )
    
    actions = ["export_as_csv"]
    export_as_csv.short_description = "Export Selected"

admin.site.register(ReportModel, ReportModelAdmin)
admin.site.register(InvolvedTech)
