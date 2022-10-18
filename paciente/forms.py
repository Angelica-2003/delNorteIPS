from dataclasses import fields

import django

from django.forms import ModelForm
from paciente.models import paciente

class pacienteform(ModelForm):
    class Meta:
        model= paciente
        exclude=['servicio']