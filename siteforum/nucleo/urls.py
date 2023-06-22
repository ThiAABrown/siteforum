from django.urls import path
from django.contrib.auth.views import LoginView


from .views import cadastrar_usuario, cadastrar_post, cadastrar_comentario, atualizar_cadastro
from . import views


urlpatterns = [
    path('cadastrousuario/', cadastrar_usuario, name='cadastro_usuario'),
    path('home/', views.home, name='home'),
    path('atualizarcadastro/', atualizar_cadastro, name='atualizar_cadastro'),
    path('cadastrarpost/', cadastrar_post, name='cadastrar_post'),
    path('cadastrarcomentario/<int:post_id>/', cadastrar_comentario, name='cadastrar_comentario'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]