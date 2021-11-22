from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.

    
class Lenguaje(models.Model):
    '''
    Lenguaje de los videojuegos
    '''
    name = models.CharField(primary_key = True, max_length=100, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

class Genre(models.Model):
    name = models.CharField("Genero",primary_key = True, max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        

class Videojuego(models.Model):
    '''Libro de aplicacion de biblioteca...'''
    title = models.CharField(primary_key = True, max_length=250)
    summary = models.TextField(blank=True)
    precio = models.CharField(max_length=20, blank=True)
    fecha = models.DateField(auto_now=True, null=True, help_text='Fecha de publicacion')
    imagen = models.ImageField(upload_to='images/logos', blank=True)
    #relaciones de autor y genero
    genre = models.ManyToManyField(Genre)
    lenguaje = models.ManyToManyField(Lenguaje)

    def __str__(self):
        return self.title

    def muestra_genero(self):
        '''Muestra genero para admin'''
        return ', '.join([gen.name for gen in self.genre.all()[:3]])
    muestra_genero.short_description = 'Genero'

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de videojuego
        """
        return reverse('videogame-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Videojuego'
        verbose_name_plural = 'Videojuegos'    
        
class User(AbstractUser):
    saldo = models.CharField(max_length=100, blank=True, null=True)
    juegosComprados = models.ManyToManyField(Videojuego, null=True, blank=True)  
    amigos = models.ManyToManyField('self', null=True, blank=True)  
    imagen = models.ImageField(upload_to='images/avatares', blank=True)

class CompraVideojuego(models.Model):
    juego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    fechaCompra = models.DateField("Fecha compra", null=True, blank=True)
    precioCompra = models.CharField(blank=True, max_length=20)
    usuarioCompra = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

