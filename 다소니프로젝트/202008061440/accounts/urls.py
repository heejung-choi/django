from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('test1/', views.test1, name='test1'),
    # path('logout/', views.logout, name='logout'),
    # path('mypage/', views.update, name='update'),
]
