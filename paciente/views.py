from django.shortcuts import render
from django.shortcuts import Form

    # TODO: Define form fields here


from paciente.forms import pacienteform

# Create your views here.

def pacientes_crear(request):
    titulo="Pacientes - Crear"
    Form= pacienteform()
    context={
        "titulo":titulo,
        "form":Form
        
    }
    return render(request,'pacientes-crear/pacientes-crear.html',context)
