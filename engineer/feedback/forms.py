from django import forms
from .models import *


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'myfield'}),
            'content': forms.Textarea(attrs={'cols': 160, 'rows': 20})
        }
