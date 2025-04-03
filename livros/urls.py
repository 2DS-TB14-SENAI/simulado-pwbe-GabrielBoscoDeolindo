from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.listar_livros),
    path('criarlivro/', views.criar_livro),
]