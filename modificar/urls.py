from django.urls import path
from modificar.views import modificar


urlpatterns = [
    path('',modificar,name='modificar')
]