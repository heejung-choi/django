## [Insta 만들기]

1. git pull 해서 06_insta

2. migrate

3. runserver ,  /posts 확인

   ------

   

   ### - <이미지 업로드 구현 하기>

   1. <models.py > - posts

   ```
   from django.db import models
   from django.conf import settings
   
   # Create your models here.
   class Post(models.Model):
       content = models.CharField(max_length=200)
       image = models.ImageField()
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       created_at = models.DateTimeField(auto_now_add=True)
   ```

- 작성하고 저장하면 에러 뜨는데, 

  `pip install pillow ` 라이브러리 설치

2. makemigrations , migrate

3. <nav.html> - insta 에 글쓰기 링크 추가하기 

```
<nav class="nav d-flex justify-content-center my-4">
  {% if user.is_authenticated %}
    <a class="nav-link" href="{% url 'posts:create' %}">글쓰기</a>
    <a class="nav-link" href="{% url 'accounts:logout' %}">로그아웃</a>
```



4. <urls.py> - post에 글쓰기 (create) path 설정

```
 path('create/', views.create, name='create'),
```



5. <forms.py>-post에  form 작성

```
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = '__all__'
        exclude = ('user',)
```



6. <views.py> - post 글쓰기 (create) 함수 작성

```
from .forms import PostForm

def create(request):
    if request.method == 'POST':
        pass
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)
```

7. <form.html> - post  출력되는 부분 작성

```
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}
    <form action="" method="POST" >
        {% csrf_token %}
        {% bootstrap_form form %}
        <!--부트스트랩 사용해서 form 출력-->
        <button class ='btn btn-primary'>저장</button>
    </form>
{% endblock  %}
```



8.  <views.py>-post 에 POST 요청 부분에  raise 구문 추가

-  raise 란? 오류 뜨는거 확인할라고 추가하심

```
def create(request):
    if request.method == 'POST':
        raise 
        #일부러 오류뜨는거 확인할라고 작성하신것
        pass
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)
```

- raise 구문 작성후,  글쓰고  파일 업로드 해보고 오류를 확인하면 ,

  FILES 부문에 No Files data 뜸

  ![캡처](https://user-images.githubusercontent.com/63486972/85642189-bd5fa600-b6cb-11ea-8ae3-341079bb9f37.PNG)

9. <form.html> - post 에 

`enctype="multipart/form-data"` 추가 후 글 작성후, 에러 확인하면

파일 data 전송된거 확인할 수 있음

```
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}
    <form action="" method="POST" enctype="multipart/form-data">
    <!--enctype="multipart/form-data" : 파일 data 전송-->
        {% csrf_token %}
        {% bootstrap_form form %}
        <!--부트스트랩 사용해서 form 출력-->
        <button class ='btn btn-primary'>저장</button>
    </form>
{% endblock  %}
```



10.  <views.py>-post 에 raise 지우고 POST 받는 부분 새로 작성

```
@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #에러 확인하면, file data가 POST 파트에 없는 거 확인 할 수 있는데
        , 그래서 두번째 아규먼트로 request.FILES 파일 데이터 저장하는 부분 넣어주어야함
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            #user 정보를 넣을때 문제가 되는 것이
            , 로그인 한 상태가 아니라면 anonymouseuser 떠서 에러 뜨는데,
            #이것을 방지해주기 위해 login_required decorator 추가 시켜줌 
            post.save()
            return redirect('posts:index')

```

- login_required  decorator 쓰려면 import 

```

from django.contrib.auth.decorators import login_required
```



11. <settings.py>에  맨 끝에 부분에 미디어 어디서 설정하고, 어디서 불러올지 작성

```
#미디어 어디서 설정하고, 불러올지
MEDIA_URL = '/media/'
#사용자에게 보여지는 주소 (URL) 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
#실제 저장되는 주소
```

12. 여기까지 한 후 글쓰고, 파일 업로드 하면,  media 라는 폴더 생긴 거 알 수 있고, 그 안에 업로드한 사진 들어가 있음

![캠](https://user-images.githubusercontent.com/63486972/85644583-5691bb00-b6d2-11ea-9f9e-4fd492d223e6.PNG)

13. 파일 data 들어가 있는지 확인하기 위해, admin 계정 생성후 확인해 보기

`python manage.py createsuperuser`

<admin.py>에  post model 등록

```
from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)
```

`python manage.py runserver` 한 후  Post model 확인하면 파일 업로드 되어 있는데,

클릭하면 404 에러뜸

-------------> Media URL 재설정 해주어야 함

14. <urls.py>- insta 에  urlpatterns 추가 (방법 3가지)

- 방법1 (우리가 원래 하던 방식 ) : [1,2,3,4]

- 방법2 : [1,2,3]+4

- 방법3: a = [1,2,3] 

  ​           a += 4

  <방법2 사용>

```
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 방법3) urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# admin 계정에서 media에서 올려진 사진 파일이 404 에러 뜨며 보이지 않을때 설정해주어야 하는 것 
# static 함수 안에 url 아규먼트 설정, path('create/', views.create) 구조와 같은 개념
```

15.  인스타처럼 게시물 보여지는 페이지 구현 index.html 과 card.html로 분리해서 작업 
    - <index.html> -posts  에 올린 post 출력 페이지 작성

```
{% extends 'base.html' %}
{% block content %}
<div class="row row-cols-3">
   <!--화면에 row, col 3개씩 보여짐-->
  {% for post in posts %}
    <div class="col mb-6">
    <!--mb : 마진-->   	
      {% include 'posts/card.html' %}
    </div>
  {% endfor %}
</div>
{% endblock %}

```

- <card.html> - post 작성 

```
<div class="card">
<!--그리드 시스템 : 약간 반응형 웹 같은-->
  <h5 class="card header">
    <img class ="rounded-circle" src="http://cdn.apsk.co.kr/news/photo/202002/34259_42819_5036.jpg"  width="50px" height="50px">{{ post.user.username }}
  </h5>

  <img src="{{ post.image.url }}" class="card-img-top" alt="..." width="300px" height="300px">
  <!--임의로 사진의 크기를 조정하면 안되는 이유? 사용자마다 일정한 크기의 사진을 올리는게 아니기 때문에 -->
  <div class="card-body">
    <i class="far fa-heart"></i>
    <p class="card-text">{{ post.content }}</p>
    <p class="card-text">{{ post.created_at }}</p>
    {% comment %} <p>{{ post.image.url }}</p>   {% endcomment %}
    <!--{{ post.image }}: 사진의 이름이 저장되어 있음(실제로는 객체임)-->
    <!--{{ post.image.url }} : 아까 사진 클릭시 보이던 url 보여짐, 이것을 위에 img scr 속성에 넣어줌-->
    
  </div>
</div>
```

- 그리드란 ? 약간 반응형 웹 같이 , 화면의 크기가 변형될 때마다 그 사이즈에 맞게 row에 넣어줌

  container  <base.html>

   	row  : container 안에  row <index.html>

16. `pip install django-imagekit `설치   ''https://pypi.org/project/django-imagekit/'' 참조

17. <settings.py> 에 installed_apps 에 

imagekit 추가

18. <views.py>-post에 post 다 listup 해주는 부분  index 수정 작성 

```
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

```

19. UI 세부 조정하기 

    - Posts에 업로드 되는 이미지 크기 조정  

      <models.py> -posts 의 이미지 필드 수정 : 이미지 500X500으로 사이즈 재조정

       -> 기존에 설정한  image = models.ImageField() 를 

      ​     image = ProcessedImageField() 로 수정

      

    - Posts를  아이디 알파벳 순으로 조정

      <models.py> -posts  의 class Meta 정보에 ordering  주기

      

    ```
    from imagekit.models import ProcessedImageField
    from imagekit.processors import ResizeToFill
    
    
    class Post(models.Model):
        content = models.CharField(max_length=200)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        #image = models.ImageField()
    
        image = ProcessedImageField(upload_to='media',
                                    processors=[ResizeToFill(500, 500)],
                                    format='JPEG',
                                    options={'quality': 60})
        #이미지 사이즈 재설정(500X500)
     
     
        class Meta:
            ordering = ['-id'] 
            #아이디 순으로 정렬
    ```

------



### -<M:N 관계 설정 하기 : 각 User가  각 Posts에 좋아요 누르는 기능>

- 하트 모양 누르면  좋아요 버튼 누르는 기능

 1번 유저가 3번게시물에 좋아요를 눌렀다는 관계 설정 (M:N관계)

 이 게시물을 좋아요 버튼 누른 사람을 저장하는 column 만들기

- 중계 모델: 장고 내부에서는 user와 post 의 관계를 설정하면서 중간 단계 테이블을 새로 생성해서 like_posts , like_users 개념을 가져온다.

  

1. <models.py>-post에 like_users 컬럼 작성

   해당 user가 어떤 게시물에 좋아요를 눌렀는지

   해당 게시물에 어떤 User들이 좋아요를  눌렀는지 관계를 설정하기 위해 ( M:N 관계 설정)

   ```
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
   ```

   -> 이렇게 관계 설정해주면 

    user.like_posts로 어떤 게시물을 좋아요 버튼 눌렀는지

    / post.like_users로 그 게시물을 좋아요 누룬 유저들을 접근할 수 있다 ! 

   

   - 1: N 구조에서 User가 

     작성한 게시물들 (ForeignKey 설정),  

     좋아요 누른 게시물들 (Many to Many 설정) 관계 설정시

     User 아래에 눈에는 보이지 않지만 자동으로 

      각각 post_set  column 들이 추가 되는데 ,  둘이 같아서 충돌 나기때문에 

     ManytoManyField 아규먼트로 `related_name='like_posts'  ` 설정 해주어야 함 

     (login 함수 이름 재설정하는 것과 같은 개념 `login as auth_login` 과 같은 개념 ) 

    

      #class User:
       #post_set = FK =>어떤유저가 작성한 글들
       #post_set = M2M => 어떤 유저가 좋아요 버튼 누른 글들 
       #둘이 같아서 충돌남 . 아래 related_name='like_posts' 로 설정 하는 순간
       #아래 post_set -> like_posts 로 변경됨.

   

   ```
   from django.conf import settings
   
   
   # Create your models here.
   
   class Post(models.Model):
       content = models.CharField(max_length=200)
      
      #작성한 사람을저장 ,어느 유저가 post 작성했는지를 저장
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       
       created_at = models.DateTimeField(auto_now_add=True)
       #image = models.ImageField()
   
       image = ProcessedImageField(upload_to='media',
                                   processors=[ResizeToFill(500, 500)],
                                   format='JPEG',
                                   options={'quality': 60})
       #이미지 사이즈 재설정(500X500)
       
       #누가 좋아요를 눌럿는지 즈장
       like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
   ```

   

2. <urls.py>-posts 에 path 설정

   ```
    path('<int:post_pk>/like/', views.like, name='like'),
   ```

   

2. <views.py>-posts에 like 함수 작성

   ```
   #로그인 되어 있으면 
   @login_required
   def like(request, post_pk):
       user = request.user
       # 지금 로그인한 유저 정보,
       post = get_object_or_404(Post, pk=post_pk)
       
       #user.like_posts : 지금 로그인한 user가 좋아요 버튼을 누른 게시물들
       #post.like_users : post 에 좋아요 버튼을 누른 유저들
       
       # 1 in [1,2,4]  : 오른쪽 배열에서 1이 있으면 true 반환 개념
       if post in user.like_posts.all(): 
           #좋아요 버튼을 이미 누른 경우
           user.like_posts.remove(post)
       else: 
           #이미 안누른 경우 -> 걍 추가 해주면 됨
           user.like_posts.add(post)
   
       return redirect('posts:index')
   
   ```

   

3. <card.html> -post 부분에 좋아요 표시 기능 구현

   <i class="far fa-heart"></i> 부분  a 태그로 감싼 후 , 

   좋아요 눌러져 있을때, 

   좋아요 눌러져 있지 않을 때로 수정.

   ```
   <div class="card">
   <!--그리드 시스템-->
     <h5 class="card-header">
     <!--프로필 사진-->
       <img class ="rounded-circle" src="http://cdn.apsk.co.kr/news/photo/202002/34259_42819_5036.jpg" width="50px" height="50px">
       {{ post.user.username }}
     </h5>
     <!--업로드된 사진-->
     <img src="{{ post.image.url }}" class="card-img-top" width="300px" height="300px">
     <!--임의로 사진의 크기를 조정하면 안되는 이유? 사용자마다 일정한 크기의 사진을 올리는게 아니기 때문에 -->
     
     
     <div class="card-body">
       {% if post in user.like_posts.all %}
         <a href="{% url 'posts:like' post.id %}"><i class="fas fa-heart fa-2x" style="color: red"></i></a>
       {% else %}
         <a href="{% url 'posts:like' post.id %}"><i class="far fa-heart fa-2x" style="color: black"></i></a>
       {% endif %}
       
       
       
       
       <p class="card-text">{{ post.content }}</p>
       <p class="card-text">{{ post.created_at }}</p>
       {% comment %} <p>{{ post.image.url }}</p>   {% endcomment %}
       <!--{{ post.image }}: 사진의 이름이 저장되어 있음(실제로는 객체임)-->
       <!--{{ post.image.url }} : 아까 사진 클릭시 보이던 url 보여짐, 이것을 위에 img scr 속성에 넣어줌-->
       
     </div>
       
   ```

   

4. <forms.py> - posts 에 like_users 도 exclude 해주기

   ```
   from django import forms
   from .models import Post
   
   class PostForm(forms.ModelForm):
       class Meta:
           model = Post
           #fields = '__all__'
           exclude = ('user', 'like_users')
   ```

   