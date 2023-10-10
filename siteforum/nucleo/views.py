from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import CustomUser, Post, Comentario
from .forms import PostForm, ComentarioForm, CadastroUsuarioForm, AtualizarUsuarioForm

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

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
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
            user.cpf = cpf
            user.endereco = endereco
            user.sexo = sexo
            user.data_nascimento = data_nascimento
            user.set_password(password)
            user.save()
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    
    else:
        form = CadastroUsuarioForm()
    
    return render(request, 'cadastro_usuario.html', {'form': form})


@login_required
def atualizar_cadastro(request):
    user = request.user
    if user.nome is None:
        user.nome = ''
    if user.sobrenome is None:
        user.sobrenome = ''
    if user.email is None:
        user.email = ''
    if user.cpf is None:
        user.cpf = ''
    if user.endereco is None:
        user.endereco = ''
    __import__('ipdb').set_trace()
    if request.method == 'POST':
        form = AtualizarUsuarioForm(request.POST, instance=user)
        if form.is_valid():
            # password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            cpf = form.cleaned_data['cpf']
            endereco = form.cleaned_data['endereco']
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            sexo = form.cleaned_data['sexo']
            data_nascimento = form.cleaned_data['data_nascimento']
            
            user.nome = nome
            user.sobrenome = sobrenome
            user.email = email
            user.cpf = cpf
            user.endereco = endereco
            user.sexo = sexo
            user.data_nascimento = data_nascimento
            # user.set_password(password)
            user.save()
            return redirect('home')
    else:
        form = CadastroUsuarioForm(instance=user)
    return render(request, 'atualizar_cadastro.html', {'form': form})

@login_required
def atualizar_senha(request):
    if request.method == 'POST':
        password = request.POST['password']
        new_password = request.POST['new_password']
        user = request.user

        # Para verificar se a senha atual do usuário é válida
        if user.check_password(password):
            # set_password() para atualizar a senha
            user.set_password(new_password)
            user.save()

            # Para autenticar o usuário novamente e mantê-lo logado
            autenticacao_user = authenticate(request, username=user.username, password=new_password)
            login(request, autenticacao_user)

            messages.success(request, 'Sua senha foi atualizada com sucesso.')
            return redirect('perfil')  # Redirecionar para a página de perfil após a atualização da senha
        else:
            messages.error(request, 'A senha atual inserida está incorreta.')
    return render(request, 'atualizar_senha.html')


@login_required
def perfil(request):
    user = request.user
    return render(request, 'perfil.html', {'user': user})

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
        'post' : Post.objects.get(id=post_id),
        'comentarios' : Comentario.objects.filter(post=post_id)
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
            return redirect('detalhe_post', post_id=post_id)  # Redirecionar para a página de detalhes do post
    else:
        form = ComentarioForm()
    
    return render(request, 'cadastrar_comentario.html', {'form': form, 'post': post})
