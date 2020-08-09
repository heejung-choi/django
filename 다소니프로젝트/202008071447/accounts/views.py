from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        # print(request.POST)
        # print(form.is_valid())
        # print(form.error_messages)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
        
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@require_http_methods(['POST',])
def logout(request):
    auth_logout(request)
    return redirect('index')

# def index(request):
#     return render(request, 'accounts/index.html')

# @login_required
# def update(request):
#     # form = CustomUserChangeForm(instance = request.user)
#     user = User.objects.get(username=request.user)
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, instance=user)
#         print(form.data)
#         print(form.errors)
#         print(form.is_valid())
#         if form.is_valid():
#             form.save()
#             return redirect('accounts:update')
#     else:
# 	    form = CustomUserChangeForm(instance=user)

#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/mypage.html', context)


