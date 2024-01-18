from .models import *
from django import forms


class FormEmergency(forms.ModelForm):
    class Meta:
        model = Incidents
        fields = '__all__'