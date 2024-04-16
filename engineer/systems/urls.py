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
    path('equipments_itp/', views.Equipments_itp, name='itp'),
    path('equipments_ov/', views.Equipments_ov, name='ov'),

    path('add_tasks/', views.Add_tasks, name='add_tasks'),
    # paths API
    path('api/v1/task_list', EquipmentsAPIView.as_view()),

]
