from django.urls import path
from listarUsuario.views import listarUsuario


urlpatterns = [
    path('',listarUsuario,name='listarUsuario')
]