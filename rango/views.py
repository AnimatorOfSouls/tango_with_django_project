from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hi! </br><a href=''>Index</a></br> <a href='rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says about! </br><a href='../'>Index</a></br> <a href='about'>About</a>")
