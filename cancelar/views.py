from django.shortcuts import render

# Create your views here.

def cancelar (request):
    context={
        
    }
    return render(request,'cancelar/cancelar.html',context)
