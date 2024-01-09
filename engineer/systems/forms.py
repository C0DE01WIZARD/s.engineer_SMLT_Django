from .models import *
from django import forms


class FormAdd(forms.ModelForm):
    class Meta:
        model = Equipment  # используемая модель
        fields = '__all__'  # какие поля использовать, показывать
