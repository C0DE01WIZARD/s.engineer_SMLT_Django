from django.urls import path
from .import views
from .views import ServiceHome

urlpatterns = [
    path('service_home_page/', ServiceHome.as_view(), name='service_home_page')


]