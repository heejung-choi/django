from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
 
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')

    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def profile(request, username):
    #User.objects.get(id=id) 
    # get_object_or_404(User, id=id)
    user_profile = get_object_or_404(get_user_model(), username=username)

    context = {
        'user_profile': user_profile
    }

    return render(request, 'accounts/profile.html', context)

@ login_required
def follow(request,user_pk):
    me = request.user   
    you = get_object_or_404(get_user_model(),pk=user_pk)

    # if 팔로우 요청이 자기 자신이면, 
    if me == you:
        return redirect('posts.index')
    
    
        
    # 누가(로그인한 사람) 누구를(you) 팔로워 하는지..
    # 상대방의 팔로워 목록에 내가 있는지, 나의 팔로워 목록에 상대방이 있는지 체크

    if you in me.follow.all():
        # you in me.follower.all(): 기준점을 어디에 두냐의 차이
        # 너를 팔로워 하고 있는 사람 목록에 내가 있는지
        # 너의 팔로워 목록에 있으면(이미 팔로우 하고있었음)
        #you.follower.remove(me)
        me.follow.remove(you)

    else:
        #아직 팔로우 안했음
        #you.follower.add(me)
        me.follow.add(you)
    return redirect('accounts:profile', you.username)