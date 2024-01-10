from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import FormAdd
from .models import *


class AddEquipments(ListView):
    model = Equipment
    template_name = "add.html"
    context_object_name = 'add_equipments'


class List_Equimpents(ListView):
    model = Equipment
    template_name = "list_equipments.html"
    context_object_name = 'list'


def main(request):
    return render(request, "main.html")


class Equipments(ListView):
    model = Systems
    template_name = "equipments.html"
    context_object_name = 'systems'


def add(request):
    "Функция добавления оборудования"
    if request.method == 'POST':
        form = FormAdd(request.POST)
        if form.is_valid():
            # print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
            try:
                form.save()
                print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
                return redirect('list_equipments')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = FormAdd()
    return render(request, 'add.html', {'form': form})  # 'form' присваем значение переменной form
