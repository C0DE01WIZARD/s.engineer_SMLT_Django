from django.urls import path
from . import views
from .views import Equipments, List_Equimpents

urlpatterns = [
    path('', views.main, name='main'),
    path('equipments/', Equipments.as_view(), name='equipments'),
    path('add/', views.add, name='add_equipments'),
    path('list_equipments/', List_Equimpents.as_view(), name='list_equipments'),
    path('add_tasks/', views.Add_tasks, name='add_tasks')
    # path('add/', AddEquipments.as_view(), name='add_equipments')

]
