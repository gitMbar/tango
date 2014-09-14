from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
# Create your views here.

def index(request):
  # Request the context of the input
  prerender = get_template('rango/index.html')
  html = prerender.render(Context({'boldmessage': "I'm bolder than bold"}))
  return HttpResponse(html)


def about(request):
  return HttpResponse("This is a project about Rango the magnificent\n<a href='/rango'>Back</a>")