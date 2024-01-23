from django.urls import path
from feedback_1.views import FeedbackFormView

urlpatterns = [
    path('feedback_1/', FeedbackFormView.as_view(), name='Feedback_1')

]
