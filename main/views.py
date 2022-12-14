from django.shortcuts import render,redirect,HttpResponse
from django.views.defaults import page_not_found
from django.contrib.auth import logout


def inicio(request):
    context={

    }
    return render(request,'index.html',context)

def pacientes(request):
    imagen= '/static/img/img1.jpeg'
    context={
        "imagen":imagen
    }
    return render(request,'pacientes-crear.html',context)

def submenu(request):
    context={}
    return render(request,'submenu.html',context)

def listar(request):
    context={}
    return render(request,'listar.html',context)

def modificarUsuario(request):
    context={}
    return render(request,'modificarUsuario.html',context)

def error_404(request,exception):
    return page_not_found(request,'404.html')

def buscar(request):
    context={}
    return render(request,'Cita/buscarCita.html',context)

# def loggedIn(request):
#     if request.user.is_authenticated:
#         respuesta:"Ingresado como"+ request.user.username
#     else:
#         respuesta:"No estas autenticado."
#         return HttpResponse(respuesta)  

def logout_user(request):
    logout(request)
    return redirect("login")

def ayuda(request):
   
    context={}

    return render(request,"ayuda.html",context)


