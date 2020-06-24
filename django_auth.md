## django_auth

### 04_django_auth 프로젝트 생성

1. app 2개 생성

   ``` python
   $ python manage.py startapp accounts
   $ python manage.py startapp todos
   ```

2. settings.py

   ``` python
   INSTALLED_APPS = [
       'accounts',
       'todos',
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ```



### [Accounts]

#### 권한(Authorization)/ 인증(Authentication)

- 권한 : 회원가입 후 회원에게 부여하는 기능

- 인증 : 회원가입이 되어있는지 확인 하는 것

  

#### signup 

``` python
$ python manage.py migrate
```

- 명령어 수행시 자동으로 user의 DB가 생성됨
- 따로 makemigrations 하지 않아도 됨
- `class AbstractUser` -> `class AbstractBaseUser`를 찾으면 우리가 알고 있는 user모델을 볼 수 있음
- https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/에서 `UserCreationForm` 참조
  - 미리 만들어진 ModelForm
  - `django.contrib.auth.forms` import 해서 form 사용
- <mark>국제화 : i18n</mark>
  - settings.py에 ko-kr 바꾸는 것 대신 사용 가능
- sha256 site
  - 비밀번호 암호화할 때 많이 사용됨
  - 같은 단어는 같은 코드로 변환 
    - 같은 비밀 번호를 사용하는 사람은 같은 코드가 나와 보안이 취약함
  - But 코드를 변환하는 경우의 수가 매우 많기 때문에 찾아내는 것은 쉽지 않음



#### login

``` python
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        # request, data 인자를 각각 넣어야 함
        if form.is_valid():
            # save를 해주는 게 아니라 검증하는 것이 목적임
            auth_login(request, form.get_user())
            return redirect('todos:index')

    else:
        form = AuthenticationForm()

    context={
        'form': form,
    }
    return render(request, 'accounts/login.html',context)
```

- form.is_valid() 후에 create의 save() 해주는게 아닌것이 차이점!!

- login 후 `개발자 도구 - 응용 프로그램(Application) - 저장소(Storage) - 쿠키(Cookies)` 에서 sessionid (일종의 발급증!)가 찍혀있으면 로그인 성공



#### logout

``` python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
```

- `import 할 때,`as로 변수명이 바뀌는 경우 경로가 같더라도 따로 분리해서 작성!!!



#### base.html

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% if user.is_authenticated %}
        <a href="{% url 'todos:index' %}">홈</a>
        <span>{{ user.username }}님 환영합니다.</span>
        <a href="{% url 'accounts:logout' %}">로그아웃</a>
    {% else %}
        <a href="{% url 'accounts:signup' %}">회원가입</a>
        <a href="{% url 'accounts:login' %}">로그인</a>
    {% endif %}
    {% block body %}
    {% endblock %}
</body>
</html>
```

- 모든 곳에서 사용할 것들은 보통 base에 작성 (nav, 회원가입 등) 
- `user.is_authenticated` : user가 인증되어 있는가?
  -  annonymousUser - False
  -  user가 존재 - True
- `{{ user }}` : context에 어떠한 정보를 넣지 않더라도 유일하게 사용가능한 변수명!
- 객체를 직접 출력하기보다는 내용을 출력하는 것이 좋음 -> user보다는 user.username



### [Todo]

#### models.py

``` python
from django.db import models
from django.conf import settings

class Todo(models.Model):
    content = models.CharField(max_length=100)
    due_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

- user = models.ForeignKey('auth.User', on_delete=models.CASCADE) 로 표현해도 됨

- user 정보를 customizing 해줘야 함

- user모델을 바꾸면 django에게 알려줘야 함 -> settings에 알려줘야 함!!

- django내부에 global_settings.py가 존재

- global settings에 이미 AUTH_USER_MODEL = 'auth.User'로 설정되어 있음

- settings.py에 AUTH_USER_MODEL = 'accounts.User'로 덮어씌우는 것

- 미리 만들어 놓은 변수는 사용 가능 -> 덮어 씌우기

- 변수로 가져와야 변수값을 그대로 사용 가능! -> 이래서 settings.AUTH_USER_MODEL로 사용

    django와 Todo를 1대 n 관계로 설정



#### index.html

##### 바꾸기 전

``` html
{% extends 'base.html' %}

{% block body %}
    <h1>INDEX</h1>
    <form action="{% url 'todos:create' %}" method="POST">
        {% csrf_token %}
        {{ form }}
        <button>저장</button>
    </form>

    <hr>

    {% for todo in todos %}
        <h5>{{ todo.content }}</h5>
    {% endfor %}

{% endblock %}
```

##### 바꾼 후

``` html
{% extends 'base.html' %}

{% block body %}
    <h1>INDEX</h1>
    <form action="{% url 'todos:create' %}" method="POST">
        {% csrf_token %}
        {{ form }}
        <button>저장</button>
    </form>

    <hr>

    {% for todo in user.todo_set.all %}
        <h5>{{ todo.content }}</h5>
    {% endfor %}

{% endblock %}
```



#### views.py

``` python
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    form = TodoForm()
    # todos = Todo.objects.all()
    # user를 기준으로 todos를 가져옴
    # index.html 안에 user.todo_set.all이 나타나기 때문에 더이상 필요 없음!
    context = {
        'form': form,
        # 'todos': todos,
    }
    return render(request, 'todos/index.html', context)

@login_required
def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        # form.save()
        # 여기까지만 하면 login한 user의 정보가 없음
        todo = form.save(commit=False)
        # 누가 작성한 글인지에 대해 파악하기 위해 잠시 멈춤
        todo.user = request.user
        todo.save()
        return redirect('todos:index')
```

- `@required_POST` 와 같이 (java의 어노테이션) 위에 `@login_required` 요청시 로그인 해야만 가능
- /todos/의 url을 안다고 하더라도 login 페이지로 이동해서 보여줌