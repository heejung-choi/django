from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)

@login_required
def like(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    # user.like_posts => user가 좋아요 버튼을 누른 게시물들
    # post.like_users => post에 좋아요 버튼을 누른 유저들
    if post in user.like_posts.all():
        # 이미 누른경우
        user.like_posts.remove(post)
    else:
        # 아직 안누른경우
        user.like_posts.add(post)
    return redirect('posts:index')
