from django.db import models

class CadastroUsuario(models.Model):
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=200)
