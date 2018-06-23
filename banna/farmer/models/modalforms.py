from django.forms import ModelForm
from django import forms

from .formsInfo import Report
from .userInfo import Farm

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Farm
        fields = '__all__'

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

