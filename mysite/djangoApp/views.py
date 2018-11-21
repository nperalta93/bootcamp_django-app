from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Estás en el index de mi primer djangoApp.")


# Create your views here.
