from django.urls import path
from . import views
from .views import Feedback

urlpatterns = [
    path('feedback/', views.AddFeedback, name='feedback'),
]
