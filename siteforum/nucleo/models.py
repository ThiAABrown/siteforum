from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nome = models.CharField(max_length=100, blank=True, null=True)
    sobrenome = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    assunto = models.CharField(max_length=255)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    categoria = models.CharField(max_length=100)
    data_postagem = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField()

    def __str__(self):
        return self.assunto

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    data_comentario = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField()

    def __str__(self):
        return f"Comentário por {self.autor} em {self.post}"
    