from django.urls import path
from .views import Emergency


urlpatterns = [
    path('emergency/', Emergency.as_view(), name='emergency')
]
