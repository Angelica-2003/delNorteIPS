from dataclasses import fields
from tkinter.tix import Form
import django

from django import forms 
from paciente.models import paciente

class pacienteform(forms.ModelForm):
    class Meta:
        model= paciente
        fields='__all__'