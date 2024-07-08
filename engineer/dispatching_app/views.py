from django.shortcuts import render


# Create your views here.

def dispatching(request):
    return render(request, 'page_dispatching.html', {'title': 'Диспетчеризация'})
