from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class horarioDisponible(models.Model):
    horaDisponible=models.CharField(max_length=45, verbose_name="Hora Disponible")

class medico(models.Model):
    class tipoDocumento(models.Model):
        CC='C.C', _('Cedula de Ciudadania')
        PP='P.P', _('Pasaporte')
        CE='C.E', _('Cedula de Extranjeria')   
    tipoDocumento=models.CharField(max_length=10, default=tipoDocumento.CC, verbose_name="Tipo de Documento")   # type: ignore # type: ignore
    numDocumento=models.CharField(max_length=45, verbose_name="Numero de Documento")
    nombres=models.TextField(max_length=45, verbose_name="nombres")
    apellidos=models.TextField(max_length=45, verbose_name="apellidos")
    email=models.CharField(max_length=45, verbose_name="Correo Electronico")
    celular=models.CharField(max_length=20, verbose_name="Celular")
    estado=models.BooleanField(max_length=10, verbose_name="Estado")
    horarioDisponible=models.ForeignKey(horarioDisponible, on_delete=models.CASCADE, verbose_name="Horario Disponible")
    #especialidad=models.ForeignKey(especialidad, on_delete=models.CASCADE, verbose_name="Especialidad")


class medicinaGeneral(models.Model):
    descripcion=models.TextField(max_length=45, verbose_name="Descripcion")
    class estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.BooleanField(max_length=10, verbose_name="Estado")
    medico=models.ForeignKey(medico, on_delete=models.CASCADE, verbose_name="Medico")

class tipoLaboratorio(models.Model):
    nombreLaboratorio=models.CharField(max_length=45, verbose_name="Nombre de Laboratorio")
    preparacionLaboratorio=models.CharField(max_length=45, verbose_name="Preparacion Laboratorio")
    class estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.BooleanField(max_length=10, verbose_name="Estado")

class especialidad(models.Model):
    nomEspecialidad=models.CharField(max_length=45, verbose_name="Nombre Especialidad")
    descripcion=models.CharField(max_length=45, verbose_name="Descripcion")
    estado=models.BooleanField(max_length=10, verbose_name="Estado")

class tipoEcografia(models.Model):
    nombreTipoEcografia=models.CharField(max_length=45, verbose_name="Nombre Tipo de Ecografia")
    descripcion=models.CharField(max_length=45, verbose_name="Descripcion")
    preparacionEcografia=models.CharField(max_length=45, verbose_name="Preparacion Ecografia")
    estado=models.CharField(max_length=45, verbose_name="Estado")


class servicio(models.Model):
    tipoEcografia=models.ForeignKey(tipoEcografia, on_delete=models.CASCADE, verbose_name="Tipo de Ecografia")
    medicinaGeneral=models.ForeignKey(medicinaGeneral, on_delete=models.CASCADE, verbose_name="Medicina General")
    tipoLaboratorio=models.ForeignKey(tipoLaboratorio, on_delete=models.CASCADE, verbose_name="Tipo de Laboratorio")
    especialidad=models.ForeignKey(especialidad, on_delete=models.CASCADE, verbose_name="Tipo de Ecografia")







