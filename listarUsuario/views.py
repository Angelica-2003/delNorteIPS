from django.shortcuts import render

# Create your views here.

def listarUsuario (request):
    context={
        
    }
    return render(request,'listarUsuario/listarUsuario.html',context)
