from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 1. new에서 보낸 데이터 받기
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. db에 저장
    # article = Article()
    # article.title = title
    # # 오른쪽이 new에서 받은 데이터
    # article.content = content
    # article.save()

    article = Article(title=title, content=content)
    #데이터가 유효한지 검사
    #인자로 들어갈 때에는 =에 공백을 넣지 않는다.
    article.save()

    #Article.objects.create(title=title, content=content)

    return redirect('articles:index')