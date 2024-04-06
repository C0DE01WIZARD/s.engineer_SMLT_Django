from django.urls import path

from . import views

urlpatterns = [
    path('dispatching_app/', views.dispatching, name='dispatching')

]
