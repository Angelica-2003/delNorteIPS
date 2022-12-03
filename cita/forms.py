from django import forms
from django.forms import ModelForm
from cita.models import Cita, Servicio, Agenda, FechaDisponible

class CitaForm(ModelForm):

    #horaCita=forms.TimeField(
    #widget=forms.widgets.TimeInput(attrs={'type':'time'})
    #)
    class Meta:
        model= Cita
        exclude=['estado,paciente']

class ServiciosForm(ModelForm):
    class Meta:
        model= Servicio
        exclude=['estado']

class AgendaForm(ModelForm):
    class Meta:
        model= Agenda
        fields='__all__'

class FechaDisponibleForm(forms.ModelForm):
    """Form definition for FechaDisponible."""

    class Meta:
        """Meta definition for FechaDisponibleform."""

        model = FechaDisponible
        fields='__all__'
