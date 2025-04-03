from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.livros),
    path('criarlivro/', views.livros),
    path('api/livros/', views.livros),
    path('api/livros/', views.livros),
]