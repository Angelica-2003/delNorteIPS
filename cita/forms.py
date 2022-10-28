from django.forms import ModelForm, widgets
from cita.models import Cita

class CitaForm(ModelForm):
    class Meta:
        model= Cita
        exclude=['estado']
        widgets={
            'fecha_cita': widgets.DateInput(attrs={'type':'date'})
        }