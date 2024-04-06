from .models import *
from django import forms
from django.core.mail import send_mail


class FormAdd(forms.ModelForm):
    class Meta:
        model = Equipment  # используемая модель
        fields = '__all__'  # какие поля использовать, показывать
    def send_email(self):
        send_mail(
            "Your Feedback",
            f"\t{self.cleaned_data['message']}\n\nThank you!",
            "usmanov-rushan@mail.ru",
            [self.cleaned_data["email_address"]],
            fail_silently=False,
        )



class FormAddTasks(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
