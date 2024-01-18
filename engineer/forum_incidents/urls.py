from django.urls import path

from forum_incidents import views
from forum_incidents.views import Emergency, Add

urlpatterns = [
    path('add_emergency/', views.Add, name='add_emergency'),
    path('emergency/', Emergency.as_view(), name='emergency')
]
