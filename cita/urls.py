from django.urls import path


from cita.views import agenda_crear, cita_crear, servicios_crear, citas_listar, citas_modificar, citas_eliminar, agenda, agenda_crear


urlpatterns = [

    path('crear/',cita_crear,name='cita-crear'),
    path('servicio/',servicios_crear,name='servicios-crear'),
    path('listar/cita/',citas_listar,name='cita-listar'),
    path('agendar/<str:pk>/<str:fecha>/',agenda_crear,name='crear-agenda'),
    path('agendar/<str:pk>/',agenda_crear,name='crear-agenda'),

    path('modificar/<int:pk>/',citas_modificar,name='citas-modificar'),
    path('eliminar/<int:pk>/',citas_eliminar,name='citas-eliminar'),

]