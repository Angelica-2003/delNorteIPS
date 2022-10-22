from django.urls import path
from cancelar.views import cancelar


urlpatterns = [
    path('',cancelar,name='cancelar')
]