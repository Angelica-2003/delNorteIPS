from dataclasses import fields

import django

from django import forms 
from paciente.models import paciente

class pacienteform(forms.ModelForm):
    class Meta:
        model= paciente
        fields='__all__'