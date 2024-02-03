from django.urls import path
from . import views
from .views import Equipments, List_Equimpents
from .views import EquipmentsAPIView

urlpatterns = [
    # paths HTML
    path('', views.main, name='main'),
    path('equipments/', Equipments.as_view(), name='equipments'),
    path('add/', views.add, name='add_equipments'),
    path('list_equipments/', views.List_Equimpents, name='list_equipments'),
    path('add_tasks/', views.Add_tasks, name='add_tasks'),

    # paths API
    path('api/v1/equipments_list', EquipmentsAPIView.as_view()),


]
