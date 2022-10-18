from django.shortcuts import render

from paciente.forms import pacienteform

# Create your views here.

def paciente_crear(request):
    titulo="Paciente - Crear"
    Form= pacienteform
    context={
        "titulo":titulo,
        "form":Form
        
    }
    return render(request,'paciente/pacientes-crear.html',context)
