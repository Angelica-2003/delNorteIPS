from django.shortcuts import render

# Create your views here.

def buscarUsuario (request):
    context={
        
    }
    return render(request,'buscarUsuario/buscarUsuario.html',context)
