from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
def say_hello(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return HttpResponse(context)

def anotherFun(request):
    return HttpResponse("Some text")