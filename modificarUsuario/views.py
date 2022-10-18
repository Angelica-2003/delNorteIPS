from django.shortcuts import render

# Create your views here.

def modificarUsuario (request):
    context={
        
    }
    return render(request,'modificarUsuario/modificarUsuario.html',context)
