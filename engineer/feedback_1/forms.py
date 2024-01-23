from time import sleep
from django.core.mail import send_mail
from django import forms


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        """Sends an email when the feedback form has been submitted."""
        sleep(2)  # Simulate expensive operation(s) that freeze Django
        send_mail(
            "Your Feedback",
            f"\t{self.cleaned_data['message']}\n\nThank you!",
            "usmanov-rushan@mail.ru",
            [self.cleaned_data["email"]],
            fail_silently=True,
        )



