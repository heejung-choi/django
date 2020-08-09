from django.shortcuts import render

def goods(request):
    return render(request,'tothers/goods.html')

def tourtip(request):
    return render(request,'tothers/tourtip.html')

def stamp(request):
    return render(request,'tothers/stamp.html')