from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import *
from documentation.forms import *
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


class Knowledge_base_detail(View):
    """Класс представление для вывода деталей страниц статей"""
    def get(self, request, slug):
        detail = AddArticle.objects.get(url_article=slug)  # get - метод который принимает один объект
        return render(request, 'knowledge_base_detail.html', {'knowlegedetail': detail})


def model_form_upload(request):
    """Функция для загрузки документов в директорию 'documentation'"""
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = DocumentForm()
    return render(request, 'documentation.html', {
        'form': form,
    })


def Manual(requests):
    """Функция-представление вывода мануала пользования сервисом"""
    return render(requests, 'manual.html', {'title': 'Инструкция'})


def Knowledge_base(request):
    model = AddArticle.objects.all()
    paginator = Paginator(model, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    knowl = {'knowl': model, 'title': 'База знаний инженерных систем', 'page_obj': page_obj}
    return render(request, 'knowledge_base.html', knowl)


def add_article(requests):
    article_list = AddArticle.objects.all()
    art = {'article': article_list}
    return render(requests, 'article_list.html', art)
