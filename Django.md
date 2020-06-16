# Django

- 서버를 개발하기 위한 프레임 워크



## Django 의 구조

- MVC - 소프트웨어 디자인 패턴
- `Django` 는 MVC와 비슷하지만 Model - Template - View : **MTV**
- M : 데이터 관리  //  T : 사용자가 보는 화면  //  V : 중간 관리자



## Django 설치 및 실행

- 설치 : 

  ```
  pip install django==2.1.15
  ```

- 설치 확인: 

  ```
  pip list
  ```

- 장고 프로젝트 만들기(처음에만 사용) : 

  ```
  django-admin startproject firstapp
  ```

- 서버 작동 : 

  ```
  python manage.py runserver
  ```

- 앱 생성 : 

  ```
  python manage.py startapp [app name]
  ```

- 명령어 기본 : 

  ```
  python manage.py ~~~~~~~
  ```



## 프로젝트 기본 구성 내용

- `__init__.py` : 해당 디렉토리를 패키지화 해주는 파일 (ex. import firstapp 가능)
- `settings.py` : 모든 설정을 관리해주는 파일
- `urls.py` : 요청 url
- `wsgi.py` : 배포할 때 사용
- `admin.py` : 관리자용 페이지를 커스터마이징 하는 파일
- `apps.py` : app 의 정보가 작성된 곳. 절대! 수정하지 않음
- `models.py` : app 에서 database 즉 `model` 을 정의하는 곳
- `test.py` : test code 를 작성하는 곳
- `views.py` : view들이 정의 되는 곳..다양한 함수 작성 (중간 관리자-젤 중요)



## Django 프로젝트 특징

- app 들의 집합 (한개의 프로젝트에 여러 app들이 존재함)
- 실제 요청을 처리하고 페이지를 보여주고 하는 것들은 이 app들의 역할
- app은 하나의 역할 및 기능 단위로 쪼개는 것이 일반적
- 작은 규모의 서비스에서는 세부적으로 나누지 는 않는다
- app 이름은 복수형으로 하는 것이 권장된다



## Django 프로젝트 진행 과정

1. 프로젝트 생성

2. 앱 생성

3. 프로젝트에 앱 등록 및 수정 : `settings.py` 파일 에서

   ```python
   INSTALLED_APPS = [
   	# 1. local apps : 최상단에 우리가 만든 앱
     # 2. 3rd party app
     # 3. django apps : 기본으로 작성된 애들
     'articles', #app 이름
     'django.contrib.admin',
     'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles', # 마지막 콤마 : 트레일링 콤마, 장고에서만 사용......파이썬에서는 사용할 수 없음
   ]
   
   # 아래처럼 변경해줘
   LANGUAGE_CODE = 'ko-kr' # 한글 적용
   
   TIME_ZONE = 'Asia/Seoul' # 서울로 시간 맞춰줌
   ```

4. `urls.py` 작성 : 

   ```python
   # articles app의 views.py import 해주기
   from articles import views
   
   urlpatterns = [
       path('admin/', admin.site.urls), # admin 은 포트 뒤에 주소
     	path('index/', views)
     	# path 라는 내장함수 사용, address+/(end slash)필수
   ]
   ```

5. `views.py` 작성 : 

   ```python
   def index(request):
       # import 된 render 함수의 필수인자 두개 사용 1. request 2. template_name
       return render(request, ???,)
   ```

6. `template ` 작성 : app안에 존재하는 `templates`에  작성되야함 

![image-20200610104612830](/Users/seho/Library/Application Support/typora-user-images/image-20200610104612830.png)







