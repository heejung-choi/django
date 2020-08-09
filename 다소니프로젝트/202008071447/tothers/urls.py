from django.urls import path
from . import views

app_name = 'tothers'

urlpatterns = [
    path('goods', views.goods, name='goods'),
    path('tourtip', views.tourtip, name='tourtip'),
]
