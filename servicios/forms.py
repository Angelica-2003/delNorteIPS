from django.forms import ModelForm
from servicios.models import servicio

class ServiciosForm(ModelForm):
    class Meta:
        model= servicio
        exclude=['estado']