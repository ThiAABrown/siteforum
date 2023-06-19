from django.urls import path

from .views import cadastrar_usuario, cadastrar_post, cadastrar_comentario
from . import views

urlpatterns = [
    path('cadastrousuario/', cadastrar_usuario, name='cadastro_usuario'),
    path('home/', views.home, name='home'),
    path('cadastrarpost/', cadastrar_post, name='cadastrar_post'),
    path('cadastrarcomentario/<int:post_id>/', cadastrar_comentario, name='cadastrar_comentario'),

]