from django.shortcuts import render


from paciente.forms import PacienteForm

# Create your views here.

def pacientes_crear(request):
    titulo="Pacientes - Crear"
    form= PacienteForm() 
    print ("hola mundo")
    context={
        "titulo":titulo,
        "form":form
        
    }
    return render(request,'pacientes-crear.html',context)
