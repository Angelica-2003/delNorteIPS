from django.shortcuts import render
from django.shortcuts import  redirect,render


from servicios.forms import ServiciosForm
from servicios.models import servicio

# Create your views here.

def servicios(request):
    titulo="Servicios"
    pacientes= servicios.objects.all()
    context={
        'titulo':titulo,
        'servicios':servicios
        
    }

    return render(request,"servicios.html",context)

def servicios_crear(request):
    titulo="Servicios - Crear"
    if request.method == "POST":
        form= ServiciosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Error")
    else:
        form= ServiciosForm()
    context={
        "titulo":titulo,
        "form":form
        
    }
    return render(request,'servicios.html',context)


