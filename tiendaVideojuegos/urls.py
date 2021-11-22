"""tiendaVideojuegos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

from tienda.views import AmigosUsuarioListView, VideojuegosListView, VideojuegosUsuarioListView, AñadirSaldo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VideojuegosListView.as_view(), name='inicio'),
    path('/<str:pk>', VideojuegosListView.as_view(), name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('misJuegos/',VideojuegosUsuarioListView.as_view(), name ='juegosUsuario'),
    path('misAmigos/', AmigosUsuarioListView.as_view(), name ='misAmigos'),
    path('añadirSaldo/<int:pk>', AñadirSaldo.as_view(), name ='añadirSaldo'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)