from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.index, name='index'),
    path('translate/', views.translate, name='translate'),
    path('weather/', views.weather, name='weather'),
    path('rankingtest', views.rankingtest, name='rankingtest'),
]
