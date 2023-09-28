from django.urls import path
from django.contrib.auth.views import LoginView


from .views import cadastrar_usuario, cadastrar_post, detalhe_post, cadastrar_comentario, atualizar_cadastro, logout_usuario
from . import views


urlpatterns = [
    path('cadastrousuario/', cadastrar_usuario, name='cadastro_usuario'),
    path('home/', views.home, name='home'),
    path('atualizarcadastro/', atualizar_cadastro, name='atualizar_cadastro'),
    path('cadastrarpost/', cadastrar_post, name='cadastrar_post'),
    path('postdetalhes/<int:post_id>', detalhe_post, name='detalhe_post'),
    path('cadastrarcomentario/', cadastrar_comentario, name='cadastrar_comentario'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_usuario, name='logout'),
]