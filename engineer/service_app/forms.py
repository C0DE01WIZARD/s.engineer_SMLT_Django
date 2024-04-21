from django import forms
from .models import *
class Form_Add_Service_Company(forms.ModelForm):
    class Meta:
        model = Service_company
        fields = '__all__'

class Form_Add_Service(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'