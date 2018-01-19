from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there parter! \n Here is the about page: " + about())

def about(request):
    return HttpResponse("Rango says here is the about page. \n Home: " + index())
