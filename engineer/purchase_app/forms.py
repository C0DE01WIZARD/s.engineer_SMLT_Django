from django import forms
from .models import *


class Form_Add_Purpase(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
