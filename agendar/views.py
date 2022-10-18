from tkinter.tix import Form
from django.shortcuts import render


# Create your views here.
def agendar(request):
    context={
        
    }
    return render(request,'agendar/agendar.html',context)



def submenu(request):
    context={
        
    }
    return render(request,'submenu/submenu.html',context)