from django.urls import path


from cita.views import cita_crear, servicios_crear


urlpatterns = [

    path('crear/cita/',cita_crear,name='cita-crear'),
    path('crear/servicio/',servicios_crear,name='servicios-crear'),




]