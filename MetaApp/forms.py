from django.forms import ModelForm
from .models import ReportModel

class ReportForm(ModelForm):
    class Meta:
        model = ReportModel
        fields = ("date", "time", "crimecategory", "platform", "description", "medialinks", "govreport")