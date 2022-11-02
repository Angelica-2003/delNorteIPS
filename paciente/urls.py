from django.urls import path


from paciente.views import pacientes, pacientes_crear


urlpatterns = [
    
    path('crear/',pacientes,name='pacientes'),
    path('paciente-crear/',pacientes_crear,name='pacientes-crear'),
    path('crear/<str:modal_status>',pacientes,name='pacientes'),


]