from django.shortcuts import render
from django.http import HttpResponse


def sayHelloToMyFriend(request):
    return HttpResponse("Hello! How're u?")
# Create your views here.
