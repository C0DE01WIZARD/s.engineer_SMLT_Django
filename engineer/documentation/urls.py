from django.urls import path
from documentation import views

urlpatterns = [
    path('documentation/', views.model_form_upload, name='documentation'),
    path('manual/', views.Manual, name='manual'),

]
