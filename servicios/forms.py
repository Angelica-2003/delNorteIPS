from django.forms import ModelForm
from servicios.models import Servicios

class ServiciosForm(ModelForm):
    class Meta:
        model= Servicios
        exclude=['estado']