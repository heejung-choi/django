from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 한번 만들어 진것은 바뀌지 않는다.
    updated_at = models.DateTimeField(auto_now=True)
    # 수정 가능하다.