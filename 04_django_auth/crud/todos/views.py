from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    form = TodoForm()
    #todos = Todo.objects.all()
    context = {
        'form' : form,
        #'todos' : todos,
    } # 모든 사람들의 것을 보고 싶다면 todo 이용 
    return render(request, 'todos/index.html', context)

@login_required
def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect('todos:index')

@login_required
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')
