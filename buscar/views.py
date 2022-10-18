from django.shortcuts import render

# Create your views here.

def buscar (request):
    context={
        
    }
    return render(request,'buscar/buscar.html',context)
