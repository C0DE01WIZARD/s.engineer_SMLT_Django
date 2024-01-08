from django.urls import path
from . import views
from .views import Equipments

urlpatterns = [
    path('', views.main, name='main'),
    path('equipments/', Equipments.as_view(), name='equipments'),
]
