from django.shortcuts import render
# from Tools.scripts.google import Translator
# Create your views here.
def index(request):
#     translator = Translator()
#     result = translator.translate('안녕', dest='ja')
#     context = {
#         "text" : result[0].text
#     }
    return render(request, 'maps/index.html', context=context)
