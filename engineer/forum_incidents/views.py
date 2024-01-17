from django.shortcuts import render
from .models import *
from django.views.generic import ListView


class Emergency(ListView):
    model = Incidents
    template_name = 'emergency.html'
    context_object_name = 'emergency'
