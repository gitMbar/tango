from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  return HttpResponse("Hello, World (From Rango)\n<a href='/rango/about'>Learn More</a>")

def about(request):
  return HttpResponse("This is a project about Rango the magnificent\n<a href='/rango'>Back</a>")