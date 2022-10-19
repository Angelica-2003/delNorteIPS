
from multiprocessing import context
from django.shortcuts import  redirect,render


from paciente.forms import PacienteForm
from paciente.models import Paciente

# Create your views here.

def paciente(request):
    titulo="Paciente"
    paciente= Paciente.objects.all()
    context={
        'titulo':titulo,
        'paciente':paciente
        
    }

def pacientes_crear(request):
    titulo="Pacientes - Crear"
    if request.method == 'POST':
        form= PacienteForm() 
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Error")
    else:
        form= PacienteForm
    context={
        "titulo":titulo,
        "form":form
        
    }
    return render(request,'pacientes-crear.html',context)
