from django.urls import path

from .views import cadastrar_usuario

urlpatterns = [
    path('cadastrousuario/', cadastrar_usuario, name='cadastro_usuario'),
]