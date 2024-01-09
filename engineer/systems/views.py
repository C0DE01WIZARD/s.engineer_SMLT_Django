from django.shortcuts import render
from django.views.generic import ListView
from.models import *


def main(request):
    return render(request, "main.html")


class Equipments(ListView):
    model = Systems
    template_name = "equipments.html"
    context_object_name = 'systems'



