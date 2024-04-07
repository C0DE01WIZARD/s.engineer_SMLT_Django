from django.urls import path

import users.views
from .views import *
from .views import EquipmentsAPIView
from systems import views

urlpatterns = [
    # paths HTML
    path('', users.views.login_user, name='login'),
    path('main/', views.main, name='main'),
    path('equipments/', views.Equipments, name='equipments'),
    path('add_equipments/', views.Add_equipments, name='add_equipments'),
    path('list_equipments_itp/', views.List_itp,
         name='list_equipments_itp'),
    path('add_tasks/', views.Add_tasks, name='add_tasks'),

    # paths API
    path('api/v1/equipments_list', EquipmentsAPIView.as_view()),

]
