from django.urls import path
from service_app import views
from service_app.views import *

urlpatterns = [
    path('service_home_page/', ServiceHome.as_view(), name='service_home_page'),
    path('service_company/', ServiceCompany.as_view(), name='service_company'),
    path('add_service_company/', views.Add_Service_Company, name='add_service_company'),

]
