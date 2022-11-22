from django import forms
from django.forms import ModelForm
from cita.models import Cita, Servicio, Agenda

class CitaForm(ModelForm):

    #horaCita=forms.TimeField(
    #widget=forms.widgets.TimeInput(attrs={'type':'time'})
    #)
    class Meta:
        model= Cita
        exclude=['estado']

class ServiciosForm(ModelForm):
    class Meta:
        model= Servicio
        exclude=['estado']

class AgendaForm(ModelForm):
    class Meta:
        model= Agenda
        fields=('__all__')
        