from django.shortcuts import render , HttpResponse


# Create your views here
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("About Me")

def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")


def add(request,first_num,second_num):
    return HttpResponse(f"The total is: {first_num + second_num}")