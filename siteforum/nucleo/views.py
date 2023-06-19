from django.shortcuts import render, redirect
from .models import CadastroUsuario, Post, Comentario

from .forms import PostForm, ComentarioForm, PostForm

def home(request):
    return render(request, 'nucleo/home.html')

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


def cadastrar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirecionar para a página inicial após cadastrar o post
    else:
        form = PostForm()
    
    return render(request, 'cadastrar_post.html', {'form': form})

def cadastrar_comentario(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('post', post_id=post_id)  # Redirecionar para a página de detalhes do post
    else:
        form = ComentarioForm()
    
    return render(request, 'cadastrar_comentario.html', {'form': form, 'post': post})