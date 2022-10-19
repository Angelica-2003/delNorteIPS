
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class TipoLaboratorio(models.Model):
    nombreLaboratorio=models.CharField(max_length=45, verbose_name="Nombre de Laboratorio")
    preparacionLaboratorio=models.CharField(max_length=45, verbose_name="Preparacion Laboratorio")
    class Estado(models.TextChoices):
        ACTIVO=True, _('Activo')
        INACTIVO=False, _('Inactivo')
    estado=models.BooleanField(choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")  # type: ignore

class Especialidad(models.Model):
    nomEspecialidad=models.CharField(max_length=45, verbose_name="Nombre Especialidad")
    descripcion=models.CharField(max_length=45, verbose_name="Descripcion")
    estado=models.BooleanField(max_length=10, verbose_name="Estado")

class HorarioDisponible(models.Model):
    horaDisponible=models.CharField(max_length=45, verbose_name="Hora Disponible")

class Medico(models.Model):
    class TipoDocumento(models.TextChoices):
        CC='C.C', _('Cedula de Ciudadania')
        PP='P.P', _('Pasaporte')
        CE='C.E', _('Cedula de Extranjeria')   
    tipoDocumento=models.CharField(max_length=10,choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")  # type: ignore
    numDocumento=models.CharField(max_length=45, verbose_name="Numero de Documento")
    nombres=models.TextField(max_length=45, verbose_name="nombres")
    apellidos=models.TextField(max_length=45, verbose_name="apellidos")
    email=models.CharField(max_length=45, verbose_name="Correo Electronico")
    celular=models.CharField(max_length=20, verbose_name="Celular")
    estado=models.BooleanField(max_length=10, verbose_name="Estado")
    horarioDisponible=models.ForeignKey(HorarioDisponible, on_delete=models.CASCADE, verbose_name="Horario Disponible")
    especialidad=models.ForeignKey(Especialidad, on_delete=models.CASCADE, verbose_name="Especialidad")

class MedicinaGeneral(models.Model):
    descripcion=models.TextField(max_length=45, verbose_name="Descripcion")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.BooleanField(max_length=10,choices=Estado.choices,default=Estado.ACTIVO, verbose_name="Estado")  # type: ignore
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name="Medico")

class TipoEcografia(models.Model):
    nombreTipoEcografia=models.CharField(max_length=45, verbose_name="Nombre Tipo de Ecografia")
    descripcion=models.CharField(max_length=45, verbose_name="Descripcion")
    preparacionEcografia=models.CharField(max_length=45, verbose_name="Preparacion Ecografia")
    estado=models.CharField(max_length=45, verbose_name="Estado")

class Servicio(models.Model):
    tipoEcografia=models.ForeignKey(TipoEcografia, on_delete=models.CASCADE, verbose_name="Tipo de Ecografia")
    medicinaGeneral=models.ForeignKey(MedicinaGeneral, on_delete=models.CASCADE, verbose_name="Medicina General")
    tipoLaboratorio=models.ForeignKey(TipoLaboratorio, on_delete=models.CASCADE, verbose_name="Tipo de Laboratorio")
    especialidad=models.ForeignKey(Especialidad, on_delete=models.CASCADE, verbose_name="Tipo de Ecografia")

class Genero(models.Model):
    class TipoGenero(models.TextChoices):
        M='M', _('Masculino')
        F='F', _('Femenino')
        NODEFINIDO='NODEFINIDO', _('No Definido')
    tipoGenero=models.CharField(max_length=10, choices=TipoGenero.choices, default=TipoGenero.NODEFINIDO, verbose_name="Tipo De Genero")  # type: ignore

class Nacionalidad(models.Model):
    nombreNacionalidad=models.TextField(max_length=45, verbose_name="Nombre de Nacionalidad")

class Paciente(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="nombres")
    apellidos=models.CharField(max_length=45, verbose_name="apellidos")
    class TipoDocumento(models.TextChoices):
        CC='C.C', _('Cedula de Ciudadania')
        TI='T.I', _('Tarjeta de Identidad')
        CE='C.E', _('Cedula de Extranjeria')
        PP='P.P', _('Pasaporte')
    tipoDocumento=models.CharField(max_length=10, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")  # type: ignore
    numDocumento=models.CharField(max_length=50, verbose_name="Numero de Documento")
    rh=models.CharField(max_length=45, verbose_name="Tipo de Sangre")
    telefono=models.CharField(max_length=20, verbose_name="Telefono")
    email=models.CharField(max_length=45, verbose_name="Correo Electronico")
    fechaNacimiento=models.DateField(verbose_name="Fecha de Nacimiento", help_text="DD/MM/AAAA")
    nombreContacto=models.CharField(max_length=45, verbose_name="Nombre Contacto Familiar")
    telefonoContacto=models.CharField(max_length=20, verbose_name="Telefono Contacto Familiar")
    clave=models.CharField(max_length=45, verbose_name="Clave de seguridad")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.BooleanField(max_length=10, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")  # type: ignore
    servicio=models.ForeignKey("servicio", on_delete=models.CASCADE, verbose_name="Servicio")
    nacionalidad=models.ForeignKey(Nacionalidad, on_delete=models.CASCADE, verbose_name="Nacionalidad")   
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Genero")
