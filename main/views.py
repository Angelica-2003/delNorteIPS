from django.shortcuts import render

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

