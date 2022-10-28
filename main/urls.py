"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import handler404
from buscarUsuario.views import buscarUsuario


from main.views import error_404, inicio, login, submenu, pacientes,listar

handler404= error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login,name='login'),
    path('inicio/',inicio,name='inicio'),
    path('index/',inicio,name='index'),
    path('submenu/',submenu,name='submenu'),
    path('inicio/',inicio,name='costo'),
    path('buscarUsuario/',listar,name='buscarUsuario'),
    path('pacientes/',include('paciente.urls')),
    path('servicios/',include('servicios.urls')),
    path('cita/',include('cita.urls')),
    path('buscar/',include('buscar.urls')),
    path('modificar/',include('modificar.urls')),
    path('cancelar/',include('cancelar.urls')),
    path('buscarUsuario/',include('buscarUsuario.urls')),

]
