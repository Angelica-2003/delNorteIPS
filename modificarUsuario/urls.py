from django.urls import path
from modificarUsuario.views import modificarUsuario


urlpatterns = [
    path('',modificarUsuario,name='modificarUsuario')
]