import requests
from pprint import pprint
from datetime import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'firstapps/index.html')

def hello(request, name):
    context = {
        'name' : name,
    }    
    return render(request, 'firstapps/hello.html', context)
