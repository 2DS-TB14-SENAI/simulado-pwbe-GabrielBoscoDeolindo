from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.listar_livros),
    path('livros/', views.criar_livro),
    path('api/livros/', views.listar_livros),
    path('api/livros/', views.criar_livro),
]