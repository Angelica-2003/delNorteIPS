from django.forms import ModelForm
from servicios.models import Servicio

class ServiciosForm(ModelForm):
    class Meta:
        model= Servicio
        exclude=['estado']