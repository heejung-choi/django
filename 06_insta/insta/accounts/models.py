from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'follower')
    # user_set
    # follower는 우리가 만들지 않았음에도 불구하고, 자동으로 생성된 것이다.
    # posts.model.py에서 relate_name은 필수이다. 여기서는 필수는 아니다.