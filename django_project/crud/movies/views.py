from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Movie, Comment
from .forms import MovieForm, CommentForm

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie': movie,
    }
    return render(request, 'movies/index.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    # http method POST 일 때
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    # POST가 아닌 다른 methods 일 때
    else: 
        form = MovieForm()
    context = {        
        'form': form,
    }
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    form = CommentForm()

    context = {
        'movie': movie,
        'form' : form,                                                                                                                            
    }
    return render(request, 'movies/detail.html', context)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    movie= Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
    }
    return render(request, 'movies/update.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    return redirect('movies:detail', movie.pk) 

def comment_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.movie = movie
        comment.save()
        
    return redirect('movies:detail', movie.pk)

def comment_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk) 