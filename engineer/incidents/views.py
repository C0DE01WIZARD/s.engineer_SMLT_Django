import json

from django.shortcuts import render, redirect

from .bot import send_message
from .models import *
from django.views.generic import ListView
from .forms import *


class Emergency(ListView):
    """Класс для оторбражения аварий на странице"""
    model = Incidents
    template_name = 'emergency.html'
    context_object_name = 'emergency'


def Add(request):
    """Функция добавления аварий"""
    if request.method == 'POST':
        form = FormEmergency(request.POST)
        form.save()

        message = ((str(form.cleaned_data).replace('date', "Дата", ).replace('times', "Время")
                    .replace("{", '').replace("}", '', ).replace('Датаtime.Дата', ''))
                   .replace('Датаtime.time', "")).replace('Датаtime.time', "")

        send_message(message + logging)
        if form.is_valid():
            try:
                form.save()
                print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
                return redirect('emergency')
            except:
                form.add_error(None, 'Ошибка добавления аварии')
    else:
        form = FormEmergency()
    return render(request, 'add_emergency.html', {'emergency': form})
