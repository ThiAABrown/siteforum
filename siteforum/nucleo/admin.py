from django.contrib import admin

from .models import CustomUser, Post, Comentario

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'sexo','data_nascimento', 'cpf', 'endereco',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('assunto', 'categoria', 'mensagem',)

    fields = ('assunto', 'categoria', 'mensagem',)

    def save_model(self, request, obj, form, change):
        # __import__('ipdb').set_trace()
        obj.autor = request.user
        super().save_model(request, obj, form, change)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('mensagem',)