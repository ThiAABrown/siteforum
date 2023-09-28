from django import forms
from .models import CustomUser, Post, Comentario

class CadastroUsuarioForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'cpf', 'endereco', 'nome', 'sobrenome', 'sexo', 'data_nascimento']
        widgets = {
            'password': forms.PasswordInput()
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['assunto', 'categoria', 'mensagem']
        widgets = {'usuario': forms.HiddenInput()}

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'mensagem']