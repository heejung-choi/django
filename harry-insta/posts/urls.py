from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('<int:post_pk>/like/', views.like, name='like'),
    path('<int:post_pk>/comment/', views.comment_create, name='comment_create'),
]
