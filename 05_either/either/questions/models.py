from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    answer_a = models.CharField(max_length=100)
    answer_b = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Answer(models.Model):
#    CHOICE = [
#        ('a', '빨강'),
#        ('b', '파랑'),
#    ]
    # chioce = models.CharField(max_length=100, choices=CpOICE)
    choice = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)