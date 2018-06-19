from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    reponse = 'Hello World'
    return HttpResponse(reponse)
