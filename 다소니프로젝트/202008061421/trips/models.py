from django.db import models
from django.conf import settings

class Tour(models.Model):
    tour_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tour_user', null=True)

class Post(models.Model):
    post_title = models.CharField(max_length=500)
    post_content = models.CharField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True)
    post_img = models.ImageField(upload_to='media')
    post_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_user', null=True)
