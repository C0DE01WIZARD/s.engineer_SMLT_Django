from django.shortcuts import render, redirect
from purchase_app.forms import Form_Add_Purpase
from purchase_app.models import Purchase
from django.views.generic import ListView


# Create your views here.

def Add_Purchase_View(request):
    """Представление для добавления и отображения закупок"""
    if request.method == 'POST':
        form = Form_Add_Purpase(request.POST)  # создаем экземпляр нашей формы и передаём POST
        if form.is_valid():  # проверка валидности формы
            try:
                form.save()
                return redirect('add_purchase')
            except:
                form.add_error(None, 'Ошибка добавления в список закупок')
    else:
        form = Form_Add_Purpase()
    return render(request, 'add_purchase.html', {'form': form})


class Purchase_list(ListView):
    model = Purchase
    template_name = 'purchase_list.html'
    context_object_name = 'list'