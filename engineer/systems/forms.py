from .models import *
from django import forms
from django.core.mail import send_mail


class FormAdd(forms.ModelForm):
    class Meta:
        model = Equipment  # используемая модель
        fields = '__all__'  # какие поля использовать, показывать

class FormAddTasks(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
