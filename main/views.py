from django.shortcuts import render

def login(request):
    context={}
    return render(request,'login.html',context)

def inicio(request):
    context={}
    return render(request,'index.html',context)

def index(request):
    context={}
    return render(request,'submenu.html',context)