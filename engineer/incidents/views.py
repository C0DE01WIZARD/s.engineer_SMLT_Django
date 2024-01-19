from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView
from .forms import *


class Emergency(ListView):
    model = Incidents
    template_name = 'emergency.html'
    context_object_name = 'emergency'


def Add(request):
    "Функция добавления аварий"
    if request.method == 'POST':
        form = FormEmergency(request.POST)
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
