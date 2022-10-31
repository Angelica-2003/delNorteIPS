
from django.forms import ModelForm
from paciente.models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model= Paciente
        exclude=['estado']
        
class PacienteUpdateForm(ModelForm):
    class Meta:
        model= Paciente
        exclude=['estado']