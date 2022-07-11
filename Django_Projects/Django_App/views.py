from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
from Django_App.models import place, mtt


def demo(request):
    obj = place.objects.all()
    obj2=mtt.objects.all()
    return render(request, "index.html", {'result': obj,'teamitem':obj2})


# def Arithmetic(request):
#     x=int(request.GET['num1'])
#     y= int(request.GET['num2'])
#     add=x+y
#     mul=x*y
#     div=y/x
#     sub=y-x
#     return render(request,"results.html",{'addition':add,
#                                          'multi':mul,
#                                          'division':div,
#                                          'subtraction':sub})
