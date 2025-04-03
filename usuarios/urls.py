from django.urls import path
from . import views

urlpatterns = [
    path('criarUsuario/', view=views.create_user, name="create_user"),
    path('logar/', view=views.login, name='login'),
]