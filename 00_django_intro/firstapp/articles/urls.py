from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('image/', views.image, name='image'),
    path('hello/<str:name>/', views.hello, name='hello'),
    # str 타입 명시는 생략 가능
    # path('hello/<name>/', views.hello),
    path('introduce/<name>/<int:age>/', views.introduce, name='introduce'),
    path('times/<int:num1>/<int:num2>/', views.times, name='times'),
    path('dtl-practice/', views.dtl_practice, name='dtl_practice'),
    path('ispal/<word>/', views.ispal, name='ispal'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('lotto-throw/', views.lotto_throw, name='lotto_throw'),
    path('lotto-catch/', views.lotto_catch, name='lotto_catch'),
    path('artii/', views.artii, name='artii'),
    path('artii-result/', views.artii_result, name='artii_result'),
]
