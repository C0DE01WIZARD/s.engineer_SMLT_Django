from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import FormAdd, FormAddTasks
from .models import *


def page_not_found(request, exception):
    message = "<h1>404 Страница не найдена</h1>"
    return HttpResponseNotFound(message)


class AddEquipments(ListView):
    model = Equipment
    template_name = "add.html"
    context_object_name = 'add_equipments'


class List_Equimpents(ListView):
    model = Equipment
    template_name = "list_equipments.html"
    context_object_name = 'list'


def main(request):
    tasks = Tasks.objects.all()
    data = {'title': 'Главная страница', 'tasks': tasks}
    return render(request, "main.html", data)


class Equipments(ListView):
    model = Systems
    template_name = "equipments.html"
    context_object_name = 'systems'


def add(request):
    "Функция добавления оборудования"
    if request.method == 'POST':
        form = FormAdd(request.POST)
        if form.is_valid():
            try:
                form.save()
                print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
                return redirect('list_equipments')
            except:
                form.add_error(None, 'Ошибка добавления оборудования')
    else:
        form = FormAdd()
    return render(request, 'add.html', {'form': form})


def Add_tasks(request):
    "Функция добавления оборудования"
    if request.method == 'POST':
        form = FormAddTasks(request.POST)
        if form.is_valid():
            try:
                form.save()
                print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
                return redirect('main')
            except:
                form.add_error(None, 'Ошибка добавления задачи')
    else:
        form_tasks = FormAddTasks()
    return render(request, 'add_tasks.html', {'form': form_tasks})
