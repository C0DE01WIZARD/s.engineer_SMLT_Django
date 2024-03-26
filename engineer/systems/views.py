from django.forms import model_to_dict
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


from .forms import FormAdd, FormAddTasks
from .models import *
from .serializers import *


# class EquipmentsAPIView(generics.ListAPIView):
#     """Класс для вывода спсика оборудования"""
#     queryset = Equipment.objects.all()
#     serializer_class = EquipmentSerializer




class EquipmentsAPIView(APIView):
    def get(self, requests):
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


def List_Equimpents(request):
    model = Equipment.objects.all()
    l = {'list': model}
    return render(request, "list_equipments.html", l)


def main(request):
    tasks = Tasks.objects.all()
    data = {'title': 'Главная страница', 'tasks': tasks}
    return render(request, "main.html", data)


class Equipments(ListView):
    model = Systems
    template_name = "equipments.html"
    context_object_name = 'systems'


def add(request):
    """Функция добавления оборудования"""
    if request.method == 'POST':
        form = FormAdd(request.POST) # создаем экземпляр нашей формы и передаём POST
        if form.is_valid(): # проверка валидности формы
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
