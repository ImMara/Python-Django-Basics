from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('article-<str:numero_article>', views.article, name='blog-article'),
]
