from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model
# get_user_model => AUTH_USER_MODEL에 적용시킨 모델 클래스 -> 내가 사용하고자 하는 유저 모델이 들어가 있다.

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', )
