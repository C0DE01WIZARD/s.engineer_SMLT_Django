from django.urls import path

from . import views

urlpatterns = [
    path('dispatching/', views.dispatching, name='dispatching')

]
