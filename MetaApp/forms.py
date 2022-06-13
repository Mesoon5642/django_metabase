from django.forms import DateInput, ModelForm, TimeInput
from .models import ReportModel

class ReportForm(ModelForm):
    class Meta:
        model = ReportModel
        fields = ("date", "time", "crimecategory", "platform", "description", "medialinks", "govreport")
        widgets = {
            "date": DateInput(attrs={'type': 'date'}),
            "time": TimeInput(attrs={"type":"time"})
        }