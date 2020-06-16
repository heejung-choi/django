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

    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 왼쪽 : article 클래스가 가진 pk , 오른쪽 variable routing 에서 보내준 값
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    print(request)
    article=Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
         'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 1. edit에서 보낸 데이터 받기
    # 기존 값에 할당
    article.title = equest.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)

