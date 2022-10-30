
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
    titulo="Crear Pacientes"
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

def pacientes_modificar(request, pk):
    titulo="Pacientes - Modificar"
    paciente= Paciente.objects.get(id=pk)
    if request.method == "POST":
        form= PacienteForm(request.POST,instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Error al guardar")
    else:
        form= PacienteForm(instance=paciente)

    context={
        "titulo":titulo,
        "form":form
        
    }
    return render(request,'modificarUsuario.html',context)

def pacientes_eliminar(request, pk):
    titulo="Pacientes - Eliminar"
    pacientes= Paciente.objects.all()
    
    
    Paciente.objects.filter(id=pk).update(
            estado= '0'
        )
    return redirect("login")
        
            

    context={
        'pacientes':pacientes,
        "titulo":titulo,
        
        
    }
    return render(request,'pacientes-crear.html',context)


