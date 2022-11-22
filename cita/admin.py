from django.contrib import admin
from .models import Cita, HoraDisponible, Agenda, FechaDisponible,Servicio

# Register your models here.
admin.site.register(Cita)
admin.site.register(HoraDisponible)
admin.site.register(Agenda)
admin.site.register(FechaDisponible)
admin.site.register(Servicio)




