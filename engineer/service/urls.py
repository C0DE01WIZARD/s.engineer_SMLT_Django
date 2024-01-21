from django.urls import path
from service import views

urlpatterns = [
    path('service_home_page/', views.ServiceHome, name='service_home_page')


]