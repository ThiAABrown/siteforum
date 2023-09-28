from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import ipdb


from .models import CustomUser, Post, Comentario
from .forms import PostForm, ComentarioForm, CadastroUsuarioForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecionar para a página inicial após o login
        else:
            return render(request, 'login.html', {'error_message': 'Credenciais inválidas.'})
    
    return render(request, 'login.html')

def logout_usuario(request):
    if request.method == 'POST' and request.user.is_authenticated:
        logout(request)
    return redirect('home')

@login_required
def atualizar_cadastro(request):
    user = request.user
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CadastroUsuarioForm(instance=user)
    return render(request, 'atualizar_cadastro.html', {'form': form})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        __import__('ipdb').set_trace()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            cpf = form.cleaned_data['cpf']
            endereco = form.cleaned_data['endereco']
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            sexo = form.cleaned_data['sexo']
            data_nascimento = form.cleaned_data['data_nascimento']
            
            user = CustomUser.objects.create_user(username=username, email=email)
            user.nome = nome
            user.sobrenome = sobrenome
            user.sexo = sexo
            user.data_nascimento = data_nascimento
            user.set_password(password)
            #__import__('ipdb').set_trace()
            user.save()
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    
    else:
        form = CadastroUsuarioForm()
    
    return render(request, 'cadastro_usuario.html', {'form': form})

@login_required
def cadastrar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('home')  # Redirecionar para a página inicial após cadastrar o post
    else:
        form = PostForm()
    
    return render(request, 'cadastrar_post.html', {'form': form})

@login_required
def detalhe_post(request, post_id):
    context = {
        'post' : Post.objects.get(id=post_id)
    }
    return render(request, 'detalhe_post.html', context)

@login_required
def cadastrar_comentario(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.post = post
            comentario.save()
            return redirect('post', post_id=post_id)  # Redirecionar para a página de detalhes do post
    else:
        form = ComentarioForm()
    
    return render(request, 'cadastrar_comentario.html', {'form': form, 'post': post})