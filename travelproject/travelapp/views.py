from django.shortcuts import render
from . models import place,news
from django.http import HttpResponse
# Create your views here.
def fun(request):
    obj=place.objects.all()
    obj1=news.objects.all()
    return render(request,"index.html",{'results':obj,'newsresults':obj1})
def addition(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    num3=num1+num2
    return render(request,"result.html",{"add":num3})