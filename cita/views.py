from django.shortcuts import render,redirect

from cita.forms import CitaForm
from cita.models import Cita

# Create your views here.

def cita(request):
    titulo="Cita"
    cita= Cita.objects.all()
    context={
        'titulo':titulo,
        'cita':cita
        
    }

    return render(request,"cita.html",context)

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
    return render(request,'cita.html',context)
