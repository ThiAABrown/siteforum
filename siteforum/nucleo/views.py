from django.shortcuts import render, redirect
from .models import CadastroUsuario

def cadastrar_usuario(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        email = request.POST['email']
        cpf = request.POST['cpf']
        endereco = request.POST['endereco']
        
        CadastroUsuario.objects.create(usuario=usuario, senha=senha, email=email, cpf=cpf, endereco=endereco)
        
        return redirect('home')
    
    return render(request, 'cadastro_usuario.html')