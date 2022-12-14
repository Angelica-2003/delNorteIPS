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


from main.views import error_404, logout_user, submenu,listar,inicio,ayuda
from django.contrib.auth.views import LoginView as login
from django.contrib.auth import views as auth_views


handler404= error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login.as_view(),name='login'),
    path('inicio/',inicio,name='inicio-adm'),
    path('submenu/',submenu,name='submenu'),
    path('buscarUsuario/',listar,name='buscarUsuario'),
    path('ayuda/',ayuda,name='ayuda'),
    path('pacientes/',include('paciente.urls')),
    path('cita/',include('cita.urls')),
    path('buscar/',include('buscar.urls')),
    path('modificar/',include('modificar.urls')),
    path('cancelar/',include('cancelar.urls')),
    path('buscarUsuario/',include('buscarUsuario.urls')),

    
    path('logout/',logout_user,name='fin-sesion'),

    path('reset_password/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_password_send/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    
    
    

    


]
