from django.forms import ModelForm

from .models import Area, Harvest, Fertilizer, Remarks

class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = '__all__'

class HarvestForm(ModelForm):
    class Meta:
        model = Harvest
        fields = '__all__'


class FertilizerForm(ModelForm):
    class Meta:
        model = Fertilizer
        fields = '__all__'

class RemarksForm(ModelForm):
    class Meta:
        model = Remarks
        fields = '__all__'


