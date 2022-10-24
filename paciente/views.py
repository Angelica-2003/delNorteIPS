
from urllib.request import Request
from django.shortcuts import  redirect,render


from paciente.forms import PacienteForm
from paciente.models import Paciente

# Create your views here.

def pacientes(request):
    titulo="Paciente"
    pacientes= Paciente.objects.all()
    context={
        'titulo':titulo,
        'pacientes':pacientes
        
    }

    return render(request,"listar.html",context)

def pacientes_crear(request):
    titulo="Pacientes - Crear"
    if request.method == "POST":
        form= PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Error")
    else:
        form= PacienteForm()
    context={
        "titulo":titulo,
        "form":form
        
    }
    return render(request,'pacientes-crear.html',context)

def modificar(request):
    titulo="Modificar Paciente"
    pacientes= Paciente.objects.all()
    context={
        'titulo':titulo,
        'pacientes':pacientes
        
    }

    return render(request,'modificarUsuario.html',context)

def pacientes_modificar(request):
    titulo="Pacientes - Modificar"
    if request.method == "POST":
        form= PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Error")
    else:
        form= PacienteForm()
    context={
        "titulo":titulo,
        "form":form
        
    }
    return render(request,'modificarUsuario.html',context)


