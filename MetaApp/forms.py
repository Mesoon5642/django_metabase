from django.forms import CheckboxSelectMultiple, DateInput, ModelForm, TimeInput
from .models import ReportModel

class ReportForm(ModelForm):
    class Meta:
        model = ReportModel
        fields = ("eventname", "date", "target", "techinvolved", "description", "mainlink")
        widgets = {
            "date": DateInput(attrs={'type': 'date'}),
            "time": TimeInput(attrs={"type": "time"}),
            "techinvolved": CheckboxSelectMultiple()
        }