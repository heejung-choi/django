
import requests
from pprint import pprint
from datetime import datetime
from django.shortcuts import render

def index(request):
    return render(request,'secondapps/index.html')
