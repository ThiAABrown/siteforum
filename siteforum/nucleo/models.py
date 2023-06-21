from django.db import models

from django.contrib.auth.models import User, AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    data_nascimento = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='user',
    )

class CadastroUsuario(models.Model):
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=200)

class Post(models.Model):
    assunto = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=100)
    data_postagem = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField()

    def __str__(self):
        return self.assunto

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_comentario = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField()

    def __str__(self):
        return f"Comentário por {self.autor} em {self.post}"