# django import style guide
# 1. standard library
# 2. 3rd party library
# 3. django
# 4. local django
 
import random
import requests
from pprint import pprint
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(foods)
    context = {
        'pick': pick,
    }
    return render(request, 'articles/dinner.html', context)


def image(request):
    image_url = 'https://picsum.photos/200/300.jpg'
    context = {
        'image_url': image_url,
    }
    return render(request, 'articles/image.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)


def introduce(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'articles/introduce.html', context)


def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1': num1,
        'num2': num2,
        'result': result,
    }
    return render(request, 'articles/times.html', context)


def dtl_practice(request):
    foods = ['짜장면', '초밥', '차돌짬뽕', '콩국수']
    empty_list = []
    messages = 'Life is short, You need Python'
    datetime_now = datetime.now()
    context = {
        'foods': foods,
        'empty_list': empty_list,
        'messages': messages,
        'datetime_now': datetime_now,
    }
    return render(request, 'articles/dtl_practice.html', context)


def ispal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    context = {
        'result': result,
    }
    return render(request, 'articles/ispal.html', context)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    # pprint(request.GET)
    # print(request.GET.get('message'))
    msg_list = ['안녕', '방가방가', '전쪽']
    message = request.GET.get('message')
    context = {
        'message': message,
        'msg_list': msg_list,
    }
    return render(request, 'articles/catch.html', context)


def lotto_throw(request):
    return render(request, 'articles/lotto_throw.html')


def lotto_catch(request):
    name = request.GET.get('name')
    numbers = range(1, 46)
    pick = sorted(random.sample(numbers, 6))
    context = {
        'name': name,
        'pick': pick,
    }
    return render(request, 'articles/lotto_catch.html', context)


def artii(request):
    response = requests.get('http://artii.herokuapp.com/fonts_list').text
    fonts_list = response.split('\n')
    context = {
        'fonts_list': fonts_list,
    }
    return render(request, 'articles/artii.html', context)


def artii_result(request):
    # 1. form에서 넘어온 데이터를 받는다.
    word = request.GET.get('word')
    font = request.GET.get('font')

    # 2. ARTII api fontlist로 요청을 보내 폰트 정보를 받는다.
    # response = requests.get('http://artii.herokuapp.com/fonts_list').text
    # print(type(response))
    
    # 3. 문자열 데이터를 리스트로 변환한다.
    # fonts_list = response.split('\n')
    # print(fonts_list)

    # 4. fonts_list에서 폰트 하나 선택
    # font = random.choice(fonts_list)
    
    ARTII_URL = f'http://artii.herokuapp.com/make?text={word}&font={font}'

    # 5. Artii api 주소로 우리가 만든 데이터와 함께 요청을 보낸다.
    result = requests.get(ARTII_URL).text

    context = {
        'result': result,
    }
    return render(request, 'articles/artii_result.html', context)