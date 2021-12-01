from django.shortcuts import redirect, render
from django.conf import settings
import os
from django.views import generic
from tienda.forms import UserForm
from tienda.models import  Genre, User, Videojuego
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
import requests
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def _datos():
    return {'genero': [l.name for l  in Genre.objects.all()]}

datos = _datos()



class VideojuegosListView(generic.ListView):
    '''
    Vista genérica para nuestro listado de autores
    '''
    model = Videojuego
    paginate_by = 8
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(VideojuegosListView, self).get_context_data(**kwargs)
        context['genero'] = datos['genero']
        return context
    
    def get_queryset(self):
        busqueda = self.request.GET.get('q')
        if busqueda:
            videojuegos = Videojuego.objects.filter(title__icontains=busqueda)
        else:
            pk = self.request.GET.get('pk')
            print(pk)
            if pk:
                videojuegos = Videojuego.objects.filter(genre__name="shooter")
            else:
                videojuegos = Videojuego.objects.all()
                
        return videojuegos
            
    
    
def VideojuegoListView(request, pk):
    if request.method == 'GET':
        videojuego = Videojuego.objects.filter(title = pk)
        datos.update({'videojuego_list': videojuego, 'pk':pk})
    elif request.method == 'POST':
        usuario = request.user
        if usuario.is_anonymous:
            messages.add_message(request, messages.SUCCESS,'Usted no ha iniciado sesion')
            return redirect('/accounts/login')
        else:
            videojuegos = Videojuego.objects.filter(title = pk)
            for videojuego in videojuegos:
                if videojuego in usuario.juegosComprados.all():
                   messages.add_message(request, messages.SUCCESS,'Usted ya tiene comprado este videojuego.')
                else:
                    if usuario.saldo >= videojuego.precio:
                        usuario.saldo = usuario.saldo - videojuego.precio
                        usuario.juegosComprados.add(videojuego)
                        messages.add_message(request, messages.SUCCESS,'Juego comprado.')
                        usuario.save()
                    else:
                     messages.add_message(request, messages.SUCCESS,'No tienes dinero suficiente.')
        
            
        return redirect('/')
    
    return render(request, 'videojuego.html', context=datos)
    
    
    
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
    success_message = " se ha añadido el saldo correctamente"
    def get_initial(self):
        return {'saldo': ''}
    
    def get_object(self):
        usuario  = super().get_object()
        self.saldoanterior = usuario.saldo
        return usuario

    def form_valid(self, form):
        saldoanterior = self.saldoanterior
        saldoanterior = saldoanterior
        nuevo = int(form.cleaned_data['saldo'])
        form.instance.saldo = saldoanterior + nuevo
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(AñadirSaldo, self).get_context_data(**kwargs)
        return context

def crear_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            passwordCi = make_password(password)
            form.instance.password = passwordCi
            form.instance.saldo = 0
            form.save()
            messages.add_message(request, messages.SUCCESS,'Usuario creado.')
            return redirect('/')
    else:
        form = UserForm()
    datos.update({'form': UserForm()})
    return render(request, 'registrarUsuario.html', context=datos)

class EliminarVideojuego(SuccessMessageMixin, generic.DeleteView):
    model = Videojuego
    success_url = '/'
    success_message = "El Videojuego se ha borrado correctamente"
    template_name = 'videojuego_confirmar_borrado.html'
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarVideojuego, self).delete(request, *args, **kwargs)
    
class ModificarVideojuego(SuccessMessageMixin, generic.UpdateView):
    model = Videojuego
    fields = '__all__'
    template_name = 'modificar_videojuego.html'
    success_url = '/'
    success_message = "%(title)s se ha modificado correctamente"