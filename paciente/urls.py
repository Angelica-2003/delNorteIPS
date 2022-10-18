from django.urls import path




from paciente.views import pacientes_crear




urlpatterns = [

    path('pacientes-crear/',pacientes_crear,name='pacientes-crear')
    
]