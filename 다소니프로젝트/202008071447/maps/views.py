from django.shortcuts import render
from googletrans import Translator
# Create your views here.
def translate(request):
    # translator = Translator()
    # result = translator.translate('안녕하세요')
    context = {
        "text" : '안녕하세요'
    }
    return render(request, 'maps/translate.html', context=context)

def index(request):
    return render(request,'maps/index.html')


def rankingtest(request):
    return render(request, 'maps/rankingtest.html')


def weather(request):
    return render(request,'maps/weather.html')