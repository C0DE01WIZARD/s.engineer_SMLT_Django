from django.shortcuts import render, redirect
from .forms import *
from .models import *



def AddFeedback(request):
    model2 = Feedback.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
        try:

            form.save()
            return redirect('main')
        except:
            form.add_error(None, 'Ошибка записи')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'feedback': form, 'model': model2})  # 'form' присваем значение переменной form
