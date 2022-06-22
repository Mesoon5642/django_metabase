from django import forms
from django.forms import CheckboxSelectMultiple, DateInput, ModelForm, TimeInput
from .models import ReportModel

class ReportForm(ModelForm):
    targetother = forms.CharField(required=False)
    cyrptoamount = forms.DecimalField(decimal_places=2, max_digits=100, required=False)
    class Meta:
        model = ReportModel
        fields = ("eventname", "date", "target", "techinvolved", "description", "mainlink", "targetother", "cryptoamount")
        widgets = {
            "date": DateInput(attrs={'type': 'date'}),
            "time": TimeInput(attrs={"type": "time"}),
            "techinvolved": CheckboxSelectMultiple()
        }