from django.urls import path
from documentation import views
from documentation.views import Knowledge_base_detail

urlpatterns = [
    path('documentation/', views.model_form_upload, name='documentation'),
    path('manual/', views.Manual, name='manual'),
    path('article_list/', views.add_article, name='article_list'),
    # База знаний ИС
    path('knowledge_base/', views.Knowledge_base, name='knowledge_base'),
    path('knowledge_base/<slug:slug>', Knowledge_base_detail.as_view(), name='knowledge_base_detail'),

]
