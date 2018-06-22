from django.forms import ModelForm
from django import forms

from .formsInfo import Harvest, Fertilizer
from .userInfo import Yield, Farm

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Farm
        fields = '__all__'

class YieldForm(ModelForm):
    class Meta:
        model = Yield
        fields = '__all__'

class HarvestForm(ModelForm):
    class Meta:
        model = Harvest
        fields = '__all__'

class FertilizerForm(ModelForm):
    class Meta:
        model = Fertilizer
        fields = '__all__'

