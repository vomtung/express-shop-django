from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def shop(request):
    return HttpResponse("Hello, world. This is shop home page")