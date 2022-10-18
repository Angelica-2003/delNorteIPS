from random import choices
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class tipoLaboratorio(models.Model):
    nombreLaboratorio=models.CharField(max_length=45, verbose_name="Nombre de Laboratorio")
    preparacionLaboratorio=models.CharField(max_length=45, verbose_name="Preparacion Laboratorio")
    class estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.BooleanField(max_length=10,choices=estado.choices, default=estado.ACTIVO, verbose_name="Estado")

class especialidad(models.Model):
    nomEspecialidad=models.CharField(max_length=45, verbose_name="Nombre Especialidad")
    descripcion=models.CharField(max_length=45, verbose_name="Descripcion")
    estado=models.BooleanField(max_length=10, verbose_name="Estado")

class horarioDisponible(models.Model):
    horaDisponible=models.CharField(max_length=45, verbose_name="Hora Disponible")

class medico(models.Model):
    class tipoDocumento(models.TextChoices):
        CC='C.C', _('Cedula de Ciudadania')
        PP='P.P', _('Pasaporte')
        CE='C.E', _('Cedula de Extranjeria')   
    tipoDocumento=models.CharField(max_length=10,choices=tipoDocumento.choices, default=tipoDocumento.CC, verbose_name="Tipo de Documento")
    numDocumento=models.CharField(max_length=45, verbose_name="Numero de Documento")
    nombres=models.TextField(max_length=45, verbose_name="nombres")
    apellidos=models.TextField(max_length=45, verbose_name="apellidos")
    email=models.CharField(max_length=45, verbose_name="Correo Electronico")
    celular=models.CharField(max_length=20, verbose_name="Celular")
    estado=models.BooleanField(max_length=10, verbose_name="Estado")
    horarioDisponible=models.ForeignKey(horarioDisponible, on_delete=models.CASCADE, verbose_name="Horario Disponible")
    especialidad=models.ForeignKey(especialidad, on_delete=models.CASCADE, verbose_name="Especialidad")

class medicinaGeneral(models.Model):
    descripcion=models.TextField(max_length=45, verbose_name="Descripcion")
    class estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.BooleanField(max_length=10,choices=estado.choices,default=estado.ACTIVO, verbose_name="Estado")
    medico=models.ForeignKey(medico, on_delete=models.CASCADE, verbose_name="Medico")

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

class genero(models.Model):
    class tipoGenero(models.TextChoices):
        M='M', _('Masculino')
        F='F', _('Femenino')
        NODEFINIDO='NODEFINIDO', _('No Definido')
    tipoGenero=models.CharField(max_length=10, choices=tipoGenero.choices, default=tipoGenero.NODEFINIDO, verbose_name="Tipo De Genero")

class nacionalidad(models.Model):
    nombreNacionalidad=models.TextField(max_length=45, verbose_name="Nombre de Nacionalidad")

class paciente(models.Model):
    nombres=models.TextField(max_length=45, verbose_name="nombres")
    apellidos=models.TextField(max_length=45, verbose_name="apellidos")
    class tipoDocumento(models.TextChoices):
        CC='C.C', _('Cedula de Ciudadania')
        TI='T.I', _('Tarjeta de Identidad')
        CE='C.E', _('Cedula de Extranjeria')
        PP='P.P', _('Pasaporte')
    tipoDocumento=models.CharField(max_length=10, choices=tipoDocumento.choices, default=tipoDocumento.CC, verbose_name="Tipo de Documento")
    numDocumento=models.CharField(max_length=50, verbose_name="Numero de Documento")
    rh=models.CharField(max_length=45, verbose_name="Tipo de Sangre")
    telefono=models.CharField(max_length=20, verbose_name="Telefono")
    email=models.CharField(max_length=45, verbose_name="Correo Electronico")
    fechaNacimiento=models.DateField(verbose_name="Fecha de Nacimiento", help_text="DD/MM/AAAA")
    nombreContacto=models.CharField(max_length=45, verbose_name="Nombre Contacto Familiar")
    telefonoContacto=models.CharField(max_length=20, verbose_name="Telefono Contacto Familiar")
    clave=models.CharField(max_length=45, verbose_name="Clave de seguridad")
    class estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.BooleanField(max_length=10, choices=estado.choices, default=estado.ACTIVO, verbose_name="Estado")
    servicio=models.ForeignKey("servicio", on_delete=models.CASCADE, verbose_name="Servicio")
    nacionalidad=models.ForeignKey(nacionalidad, on_delete=models.CASCADE, verbose_name="Nacionalidad")   
    genero=models.ForeignKey(genero, on_delete=models.CASCADE, verbose_name="Genero")
