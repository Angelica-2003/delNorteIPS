from django.urls import path

from paciente.views import pacientes_crear



urlpatterns = [
    path('crear/',pacientes_crear,name='pacientes-crear')
    
]