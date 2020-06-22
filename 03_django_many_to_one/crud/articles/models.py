from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # commant_set = 

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTime 
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id
    # 1의 관계를 지울 때 n의 관계를 어떻게 할까? CASCADE : 종속의 의미
    # 1을 지울 때 n의 것을 다 지워준다.