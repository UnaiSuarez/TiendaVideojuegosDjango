from django.shortcuts import redirect, render
from django.conf import settings
import os
from django.views import generic
from tienda.models import CompraVideojuego, Genre, User, Videojuego
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def _datos():
    return {'genero': [l.name for l  in Genre.objects.all()]}

datos = _datos()



class VideojuegosListView(generic.ListView):
    '''
    Vista genérica para nuestro listado de autores
    '''
    model = Videojuego
    paginate_by = 6
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(VideojuegosListView, self).get_context_data(**kwargs)
        context['genero'] = datos['genero']
        return context
    
    
class VideojuegosUsuarioListView(LoginRequiredMixin, generic.ListView):
    '''
    Vista genérica para nuestro listado de autores
    '''
    model = User
    paginate_by = 6
    template_name = 'juegosDelUsuario.html'
    
class AmigosUsuarioListView(LoginRequiredMixin, generic.ListView):
    '''
    Vista genérica para nuestro listado de autores
    '''
    model = User
    paginate_by = 6
    template_name = 'amigos.html'
    
class AñadirSaldo(SuccessMessageMixin, generic.UpdateView):
    model = User
    fields = ['saldo']
    template_name = 'añadirSaldo.html'
    success_url = '/'
    success_message = " se ha modificado correctamente"
    def form_valid(self, form):
        saldo = int(self.object.saldo)
        nuevo = int(form.cleaned_data['saldo'])
        print(nuevo)
        form.instance.saldo = str(saldo + nuevo)
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super(AñadirSaldo, self).get_context_data(**kwargs)
        return context