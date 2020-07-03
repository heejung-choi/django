from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (
    require_http_methods,
    require_safe,
    require_POST,
)
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
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
        'form': form,
    }
    return render(request, 'posts/create.html', context)


@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    user = request.user

    if post.like_users.filter(pk=user.pk).exists():
        post.like_users.remove(user)
        liked = False
    else:
        post.like_users.add(user)
        liked = True
    context = {
        'liked': liked,
    }
    return JsonResponse(context)


@require_safe
def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment_form = CommentForm()
    comments = post.comment_set.filter(parent__isnull=True)
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'posts/detail.html', context)


@require_POST
def comment_create(request, post_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    post = get_object_or_404(Post, pk=post_pk)
    comment_form = CommentForm(request.POST)
    comments = post.comment_set.filter(parent__isnull=True)
    parent_pk = request.POST.get('parent_pk')
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        if parent_pk:
            comment.parent_id = parent_pk
        comment.save()
    return redirect('posts:detail', post_pk)
    # context = {
    #     'comment_form': comment_form,
    #     'post': post,
    #     'comments': comments,
    # }
    # return render(request, 'posts/detail.html', context)
