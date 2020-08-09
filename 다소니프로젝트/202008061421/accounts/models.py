from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    name_kr = models.CharField(max_length=10)
    stamp = models.CharField(max_length=500)
