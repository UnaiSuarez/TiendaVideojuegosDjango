from django.contrib import admin
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import  Genre, TarjetaRegalo, Videojuego, Lenguaje, User, ImagenVideojuego, VideoVideojuego

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

@admin.register(VideoVideojuego)
class VideoVideojuegoAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ImagenVideojuego)
class ImagenVideojuego(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(TarjetaRegalo)
class TarjetaRegaloAdmin(admin.ModelAdmin):
    list_display = ['saldo','codigo','habilitado']



