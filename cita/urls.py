from django.urls import path


from cita.views import cita_crear


urlpatterns = [

    path('crear/',cita_crear,name='cita-crear'),




]