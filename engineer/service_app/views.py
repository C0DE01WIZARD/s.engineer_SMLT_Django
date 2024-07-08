from django.shortcuts import render, redirect
from django.views.generic import ListView

from service_app.forms import Form_Add_Service, Form_Add_Service_Company
from service_app.models import *


class ServiceHome(ListView):
    model = Maintenance
    template_name = 'service_home_page.html'
    context_object_name = 'service_list'


def Add_Service(request):
    """Функция добавления технического обслуживания"""
    if request.method == 'POST':
        form = Form_Add_Service(request.POST)
        if form.is_valid():
            try:
                form.save()
                print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
                return redirect('service_home_page')
            except:
                form.add_error(None, 'Ошибка добавления задачи')
    else:
        form_add_service = Form_Add_Service()
    return render(request, 'add_service.html', {'form': form_add_service})


class ServiceCompany(ListView):
    model = Service_company
    template_name = 'service_company.html'
    context_object_name = 'service_company'

def Add_Service_Company(request):
    "Функция добавления сервисных компаний"
    if request.method == 'POST':
        form = Form_Add_Service_Company(request.POST)
        if form.is_valid():
            try:
                form.save()
                print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
                return redirect('service_company')
            except:
                form.add_error(None, 'Ошибка добавления')
    else:
        form_add_service_company = Form_Add_Service_Company()
    return render(request, 'add_service_company.html', {'form': form_add_service_company})
