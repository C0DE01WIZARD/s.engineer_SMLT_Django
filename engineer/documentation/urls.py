from django.urls import path
from documentation import views

urlpatterns = [
    path('documentation/', views.model_form_upload, name='documentation'),
    path('manual/', views.Manual, name='manual'),
    path('article_list/', views.add_article, name='article_list'),
    #База знаний ИС
    path('knowledge_base/', views.Knowledge_base, name='knowledge_base'),

]
