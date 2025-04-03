from django.urls import path
from . import views

urlpatterns = [
    path('criarusuario/', view=views.create_user, name="create_user"),
    path('logar/', view=views.login, name='login'),
]