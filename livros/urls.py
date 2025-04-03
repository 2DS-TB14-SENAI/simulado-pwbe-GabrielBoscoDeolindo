from django.urls import path
from . import views

urlpatterns = [
    path('/api/livros/', views.listar_livros),
    path('/api/criarlivro/', views.criar_livro),
]