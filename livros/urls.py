from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.listar_livros),
    path('criarlivro/', views.criar_livro),
    path('api/livros/', views.listar_livros),
    path('api/criarlivro/', views.criar_livro),
]