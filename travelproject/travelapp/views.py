from django.shortcuts import render
from .models import Place, DP
# Create your views here.
from django.http import HttpResponse
def demo(request):
    #name='jinja format'
    obj=Place.objects.all()
    obj1=DP.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})

#def about(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #result=x+y
    #return render(request,'about.html',{'key':result})
#def contact(request):
    #return HttpResponse('hello its contact')'''