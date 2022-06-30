from ast import Pass
from django import forms
from django.forms import CheckboxSelectMultiple, DateInput, HiddenInput, ModelForm, PasswordInput, TimeInput
from .models import EvidenceModel, RelevantLocationModel, ReportModel, AdminUserModel, SuspectModel

class ReportForm(ModelForm):
    targetother = forms.CharField(required=False, label="Other Target")
    cryptoamount = forms.DecimalField(required=False, decimal_places=2, max_digits=100)
    class Meta:
        model = ReportModel
        fields = ("eventname", "date", "target", "techinvolved", "description", "mainlink", "targetother", "cryptoamount")
        widgets = {
            "date": DateInput(attrs={'type': 'date'}),
            "time": TimeInput(attrs={"type": "time"}),
            "techinvolved": CheckboxSelectMultiple(),
            "description": forms.Textarea(attrs={'rows': 5})
        }
class LoginForm(ModelForm):
    class Meta:
        model = AdminUserModel
        fields = ("username", "password")
        widgets = {
            "password": PasswordInput()
        }
class CreateAccountForm(ModelForm):
    confirmpassword = forms.CharField(label="Confirm Password")
    realname = forms.CharField(label="Full Name")
    class Meta:
        model = AdminUserModel
        fields = ("realname", "username", "password", "confirmpassword")
        widgets = {
            "password": PasswordInput(),
            "confirmpassword": PasswordInput()
        }
class RelevantLocationForm(ModelForm):
    class Meta:
        model = RelevantLocationModel
        fields = ("name", "description")
        widgets = {
            "description": forms.Textarea(attrs={'rows': 5})
        }
class EvidenceForm(ModelForm):
    class Meta:
        model = EvidenceModel
        fields = ("name", "datefound", "description")
        widgets = {
            "datefound": DateInput(attrs={'type': 'date'})
        }
class SuspectForm(ModelForm):
    class Meta:
        model = SuspectModel
        fields = ("name", "description", "age", "guilty")
        widgets = {
            "description": forms.Textarea(attrs={'rows': 5})
        }