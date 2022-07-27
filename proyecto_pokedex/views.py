from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, context, loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    render1 = template.render({})
    return HttpResponse(render1)

