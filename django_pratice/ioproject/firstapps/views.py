import requests
from pprint import pprint
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse  

# Create your views here.

def index(request):
    return render(request,'firstapps/index.html')

def hello(request, name):
    context = {
        'name' : name,
    }    
    return render(request, 'firstapps/hello.html', context)

def user(request):
    username = request.GET['username']
    url = 'https://api.github.com/users/%s' % username
    response = requests.get(url).json()
    return JsonResponse(response)