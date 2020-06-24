# django_either

### User 모델

- 안에 아무것도 없음

| User | AbstractUser | AbstractBaseUser |
| ---- | ------------ | ---------------- |
|      | username     | password         |
|      | first_name   | last_login       |

User -> AbstractUser 상속 -> AbstractBaseUser 상속

- django가 걸려있는 user의 모델이 있음
- User를 customUser로 사용하고 싶으면,
  - UserCreationForm의 연결관계를 바꾸거나 
  - Form자체를 새로 만들어야 함

- User에 새로운 데이터를 추가하는 것을 django는 별로 원치 않음
  - 새로운 클래스를 만들어서 넣고 싶은 데이터들을 넣음
  - <mark>1대 1 관계설정을 함</mark>



https://docs.djangoproject.com/en/3.0/topics/auth/customizing/

```bash
python manage.py makemigrations
python manage.py migrate
```



## django UserCreationForm 구조



<img width="300" height="500" alt="캡처" src="https://user-images.githubusercontent.com/58652391/85488538-6e513c80-b609-11ea-8e9a-3040ca6169df.PNG">