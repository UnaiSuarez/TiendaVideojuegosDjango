from django.contrib import admin
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import CompraVideojuego, Genre, Videojuego, Lenguaje, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','saldo']

@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ['title', 'muestra_genero', 'precio', 'fecha']
    list_filter = ['genre', 'lenguaje']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Lenguaje)
class LenguajeAdmin(admin.ModelAdmin):
    pass

@admin.register(CompraVideojuego)
class CompraVideojuegoAdmin(admin.ModelAdmin):
        list_display = ['juego','usuarioCompra']


