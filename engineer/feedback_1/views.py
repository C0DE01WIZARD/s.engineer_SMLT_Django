from django.shortcuts import render
from django.views.generic import FormView
from feedback_1.forms import FeedbackForm


# Create your views here.
class FeedbackFormView(FormView):
    template_name = "feedback_1.html"
    a = form_class = FeedbackForm
    success_url = '/main/'
    extra_context = {a: 'form'}

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
