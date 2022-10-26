from django.forms import ModelForm
from cita.models import Cita

class CitaForm(ModelForm):
    class Meta:
        model= Cita
        exclude=['estado']