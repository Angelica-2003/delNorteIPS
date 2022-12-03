from django.urls import path


from paciente.views import pacientes, pacientes_crear,pacientes_terminos


urlpatterns = [
    
    path('crear/',pacientes,name='pacientes'),
    path('paciente-crear/',pacientes_crear,name='pacientes-crear'),
    path('paciente-terminos/',pacientes_terminos,name='pacientes-terminos'),
    path('crear/<str:modal_status>',pacientes,name='pacientes'),


]