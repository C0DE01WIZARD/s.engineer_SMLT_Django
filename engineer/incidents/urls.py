from django.urls import path

from incidents import views
from incidents.views import Emergency, Add

urlpatterns = [
    path('add_emergency/', views.Add, name='add_emergency'),
    path('emergency/', Emergency.as_view(), name='emergency')
]
