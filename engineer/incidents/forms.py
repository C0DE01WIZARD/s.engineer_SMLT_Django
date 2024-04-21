from .models import *
from django import forms


class FormEmergency(forms.ModelForm):
    class Meta:
        model = Incidents
        fields = '__all__'

class FormAddDefects(forms.ModelForm):
    class Meta:
        model = Defect
        fields = '__all__'
