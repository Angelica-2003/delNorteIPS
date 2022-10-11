from django.shortcuts import render
def agendar(request):
    context={}
    return render(request,'agendar/agendar.html',context)
# Create your views here.
