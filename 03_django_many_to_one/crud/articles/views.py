from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else: 
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    form = CommentForm()
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
            # 비어있는 곳에 저장하는 것 
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        # 비어있는 곳을 보내주는 것
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index') 

@require_POST
def comment_create(request, pk):
    # if request.method == 'POST':를 해도 되지만 어차피 여기에는 post 방식만 되기 때문에
    # @require_POST을 해준다.
    article = Article.objects.get(pk=pk) # 오른쪽의 pk가 request옆의 pk다
    #content = request.POST.get('content')
    #Comment.objects.create(article=article, content=content)
    # = 뒤에 있는 변수가 위에 선언한 변수
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()        
        print(comment)
        #  print(comment) -> Comment object (None) 이라고 나온다.
        # save를 하기 전에 상태가 있었는데 , aricle object non이라는 상태이다.
        # commit=False가 해당 역할을 해준다.
        # 어떤 article에 속할지..?

    
    return redirect('articles:detail', pk)                                                         

def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk) 