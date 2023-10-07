from django.urls import path
from django.contrib.auth.views import LoginView


from .views import cadastrar_usuario, cadastrar_post, detalhe_post, cadastrar_comentario, atualizar_cadastro, logout_usuario, atualizar_senha
from . import views


urlpatterns = [
    path('home/', views.home, name='home'), # Exemplo de Impot na mesma linha
    path('perfil/', views.perfil, name='perfil'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('cadastrousuario/', cadastrar_usuario, name='cadastro_usuario'),
    path('atualizarcadastro/', atualizar_cadastro, name='atualizar_cadastro'),
    path('atualizarsenha/', atualizar_senha, name='atualizar_senha'),
    path('cadastrarpost/', cadastrar_post, name='cadastrar_post'),
    path('postdetalhes/<int:post_id>', detalhe_post, name='detalhe_post'),
    path('cadastrarcomentario/<int:post_id>', cadastrar_comentario, name='cadastrar_comentario'),
    path('logout/', logout_usuario, name='logout'),
]