from django.urls import path


from cita.views import cita_crear, servicios_crear, citas_listar, citas_modificar, citas_eliminar, agenda


urlpatterns = [

    path('crear/cita/',cita_crear,name='cita-crear'),
    path('crear/servicio/',servicios_crear,name='servicios-crear'),
    path('listar/cita/',citas_listar,name='cita-listar'),
    path('crear/agenda/',agenda,name='agenda-crear'),
    path('modificar/<int:pk>/',citas_modificar,name='citas-modificar'),
    path('eliminar/<int:pk>/',citas_eliminar,name='citas-eliminar'),





]