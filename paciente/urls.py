from django.urls import path
from buscarUsuario.views import buscarUsuario




from paciente.views import pacientes_crear, pacientes, modificar, buscarUsuario


urlpatterns = [

    path('crear/',pacientes_crear,name='pacientes-crear'),
    path('listar/',pacientes,name='pacientes-listar'),
    path('modificar/',modificar,name='pacientes-modificar'),
    path('buscar/',buscarUsuario,name='buscarUsuario'),


]