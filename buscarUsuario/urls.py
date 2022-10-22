from django.urls import path
from buscarUsuario.views import buscarUsuario


urlpatterns = [
    path('',buscarUsuario,name='buscarUsuario')
]