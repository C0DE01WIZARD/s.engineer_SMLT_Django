from django.urls import path
from purchase_app import views
from .views import Purchase_list

urlpatterns = [
    path('add_purchase/', views.Add_Purchase_View, name='add_purchase'),
    path('purchase_list/', Purchase_list.as_view(), name='purchase_list'),

]
