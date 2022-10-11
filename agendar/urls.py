
from django.urls import path

from agendar.views import agendar


urlpatterns = [
    path('',agendar,name='agendar')
]