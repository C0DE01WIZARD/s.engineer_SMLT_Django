from django.urls import path
from service_app.views import *

urlpatterns = [
    path('service_home_page/', ServiceHome.as_view(), name='service_home_page')


]