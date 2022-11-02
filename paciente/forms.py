
from django.forms import ModelForm,widgets
from paciente.models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model= Paciente
        exclude=['estado','user']
        widgets={
            'fechaNacimiento': widgets.DateInput(attrs={'type':'date'})
        }
        
class PacienteUpdateForm(ModelForm):
    class Meta:
        model= Paciente
        exclude=['estado','user']