from django import forms
from .models import *
class Form_Add_Service(forms.ModelForm):
    class Meta:
        model = Service_company
        fields = '__all__'