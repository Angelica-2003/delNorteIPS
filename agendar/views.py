from django.shortcuts import render
def inicio(request):
    context={}
    return render(request,'index1.html',context)
# Create your views here.
