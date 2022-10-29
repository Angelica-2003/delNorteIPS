from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Servicio(models.Model):
    nombre=models.CharField(max_length=45, verbose_name="Nombres de tipo de servicios")
    descripcion=models.TextField(max_length=400, verbose_name="Descripcion de los servicios")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.BooleanField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO, verbose_name="Estado")  # type: ignore
    def __str__(self)->str:
        return "%s" %(self.nombre)

class Cita(models.Model):
    servicio=models.ForeignKey(Servicio, on_delete=models.CASCADE, verbose_name="Servicio")
    fechaCita=models.DateField(verbose_name="Fecha de la Cita")
    horaCita=models.TimeField(verbose_name="Hora de la Cita")
    #costo=models.CharField(max_length=45, verbose_name="Precio de la Cita")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.BooleanField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO, verbose_name="Estado")  # type: ignore
    #funcionario=models.ForeignKey(funcionario, on_delete=models.CASCADE, verbose_name="Funcionario")
