from django.shortcuts import render
from django.views.defaults import page_not_found

def login(request):
    imagen= '/static/img/IMGprin.jfif'
    context={
        "imagen":imagen
    }
    return render(request,'login.html',context)

def inicio(request):
    context={}
    return render(request,'index.html',context)

def pacientes(request):
    imagen= '/static/img/IMGprin.jfif'
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

def servicios(request):
    context={}
    return render(request,'servicios.html',context)

