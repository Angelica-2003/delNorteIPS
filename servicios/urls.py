from django.urls import path


from servicios.views import servicios_crear


urlpatterns = [

    path('crear/',servicios_crear,name='servicios-crear'),




]