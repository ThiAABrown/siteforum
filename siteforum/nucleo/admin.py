from django.contrib import admin

from .models import CustomUser, Post, Comentario

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'sexo','data_nascimento', 'cpf', 'endereco',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # http://127.0.0.1:8000/admin/nucleo/post/
    list_display = ('assunto', 'categoria', 'autor', 'mensagem',)

    # http://127.0.0.1:8000/admin/nucleo/post/1/change/
    # http://127.0.0.1:8000/admin/nucleo/post/add/
    fields = ('assunto', 'categoria', 'mensagem',)

    def save_model(self, request, obj, form, change):
        # __import__('ipdb').set_trace()
        obj.autor = request.user
        super().save_model(request, obj, form, change)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('post', 'autor', 'mensagem',)

    fields = ('post', 'mensagem',)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)