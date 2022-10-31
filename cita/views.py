from django.shortcuts import render,redirect
from urllib.request import Request
from cita.forms import CitaForm, ServiciosForm
from cita.models import Cita, Servicio

# Create your views here.

def cita(request):
    titulo="Cita"
    cita= Cita.objects.all()
    context={
        'titulo':titulo,
        'cita':cita
        
    }

    return render(request,"Cita/cita.html",context)

def cita_crear(request):
    titulo="Agenda tu Cita"
    if request.method == "POST":
        form= CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Error")
    else:
        form= CitaForm()
    context={
        "titulo":titulo,
        "form":form
        
    }
    return render(request,'Cita/cita.html',context)

def servicio(request):
    titulo="Servicios"
    servicios= Servicio.objects.all()
    context={
        'titulo':titulo,
        'servicios':servicios
        
    }

    return render(request,"Cita/servicios.html",context)

def servicios_crear(request):
    titulo="Crear Servicio"
    if request.method == "POST":
        form= ServiciosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        else:
            print("Error")
    else:
        form= ServiciosForm()
    context={
        "titulo":titulo,
        "form":form
        
    }
    return render(request,'Cita/servicios.html',context)

def citas_listar(request):
    titulo="Cita-listar"
    citas= Cita.objects.all()
    context={
        'titulo':titulo,
        'citas':citas
        
    }

    return render(request,"Cita/buscarCita.html",context)

def modificar(request):
    titulo="Modificar Cita"
    citas= Cita.objects.all()
    context={
        'titulo':titulo,
        'citas':citas
        
    }

    return render(request,'Cita/modificarCita.html',context)

def citas_modificar(request, pk):
    titulo="Modifica tu cita"
    cita= Cita.objects.get(id=pk)
    if request.method == "POST":
        form= CitaForm(request.POST,instance=cita)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Error al guardar")
    else:
        form= CitaForm(instance=cita)

    context={
        "titulo":titulo,
        "form":form
        
    }
    return render(request,'Cita/modificarCita.html',context)

def citas_eliminar(request, pk):
    titulo="Eliminar Cita"
    pacientes= Cita.objects.all()
    
    
    Cita.objects.filter(id=pk).update(
            estado= '0'
        )
    return redirect("login")
