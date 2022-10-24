from django.urls import path


from paciente.views import pacientes_crear, pacientes, modificar,pacientes_modificar


urlpatterns = [

    path('crear/',pacientes_crear,name='pacientes-crear'),
    path('listar/',pacientes,name='pacientes-listar'),
    path('modificar/<int:pk>/',pacientes_modificar,name='pacientes-modificar'),


]