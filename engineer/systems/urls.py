from django.urls import path
from . import views
from .views import Equipments, AddEquipments


urlpatterns = [
    path('', views.main, name='main'),
    path('equipments/', Equipments.as_view(), name='equipments'),
    path('add/', views.add, name='add_equipments'),
    # path('add/', AddEquipments.as_view(), name='add_equipments')

]
