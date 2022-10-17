from django.urls import path
from buscar.views import buscar


urlpatterns = [
    path('',buscar,name='buscar')
]