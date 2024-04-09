from django.forms import model_to_dict
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import FormAdd, FormAddTasks
from .models import *
from .serializers import *


class EquipmentsAPIView(APIView):
    """Метод за отбработку GET запросов"""
    def get(self, request):
        tasks_list = Tasks.objects.all().values()
        return Response({'ЗАДАЧИ': list(tasks_list)})

    def post(self, requests):
        tasks_new = Tasks.objects.create(
            tasks=requests.data['tasks'],
            datetime=requests.data['datetime'],
        )
        return Response({'post': model_to_dict(tasks_new)})


def page_not_found(request, exception):
    message = "<h1>404 Страница не найдена</h1>"
    return HttpResponseNotFound(message)


class AddEquipments(ListView):
    model = Equipment
    template_name = "add.html"
    context_object_name = 'add_equipments'


class Filter_Address:
    """Фильтры по адресам"""

    def get_addres(self):
        return Address.objects.all()

    # class List_Equipments(Filter_Address, ListView):


def List_itp(request):
    model = Equipment.objects.all()
    l = {'list': model, 'title': 'Оборудование ИТП'}
    return render(request, "itp.html", l)


def main(request):
    tasks = Tasks.objects.all()
    data = {'title': 'Главная страница', 'tasks': tasks}
    return render(request, "main.html", data)


def Equipments(request):
    return render(request, 'equipments.html', {'title': 'Оборудование'})


def Add_equipments(request):
    """Функция добавления оборудования"""
    if request.method == 'POST':
        form = FormAdd(request.POST)  # создаем экземпляр нашей формы и передаём POST
        if form.is_valid():  # проверка валидности формы
            try:
                form.save()
                return redirect('list_equipments_itp')
            except:
                form.add_error(None, 'Ошибка добавления оборудования')
    else:
        form = FormAdd()
    return render(request, 'add.html', {'form': form})


def Add_tasks(request):
    tasks = Tasks.objects.all()
    """Функция для добавления задач"""
    if request.method == 'POST':
        form = FormAddTasks(request.POST)
        if form.is_valid():
            try:
                form.save()
                print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
                return redirect('add_tasks')
            except:
                form.add_error(None, 'Ошибка добавления задачи')
    else:
        form_tasks = FormAddTasks()
    return render(request, 'add_tasks.html', {'form': form_tasks, 'tasks': tasks})
