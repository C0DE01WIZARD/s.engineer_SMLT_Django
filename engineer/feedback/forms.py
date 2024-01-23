from django import forms
from .models import *


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback  # используемая модель
        fields = '__all__'  # какие поля использовать, показывать


