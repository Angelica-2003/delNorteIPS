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

def cita_listar(request):
    titulo="Cita-listar"
    pacientes= Cita.objects.all()
    context={
        'titulo':titulo,
        'cita':cita
        
    }

    return render(request,"buscarCita.html",context)
