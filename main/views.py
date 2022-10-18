from django.shortcuts import render

def login(request):
    context={}
    return render(request,'login.html',context)

def inicio(request):
    context={}
    return render(request,'index.html',context)

def pacientes(request):
    context={}
    return render(request,'pacientes-crear.html',context)

def submenu(request):
    context={}
    return render(request,'submenu.html',context)