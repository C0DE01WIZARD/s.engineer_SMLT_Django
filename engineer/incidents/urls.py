from django.urls import path

from incidents import views
from incidents.views import Emergency, Defect_list

urlpatterns = [
    path('add_emergency/', views.Add, name='add_emergency'),
    path('emergency/', Emergency.as_view(), name='emergency'),

    path('defect_list/', Defect_list.as_view(), name='defect_list'),
    path('add_defect/', views.Add_Defect, name='add_defect')
]
