from django.urls import path




from paciente.views import pacientes_crear, pacientes, modificar


urlpatterns = [

    path('crear/',pacientes_crear,name='pacientes-crear'),
    path('listar/',pacientes,name='pacientes-listar'),
    path('modificar/',modificar,name='pacientes-modificar'),


]