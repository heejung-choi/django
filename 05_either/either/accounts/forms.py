from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model

#User == get_user_model()
#model.py에 만들었던 user를 그대로 반환해 준다.
#get_user_model => AUTH_USER_MODEL에 적용시킨 모델 클래스ㅏㅏㅐㅐ90

class CustomUserCreationForm(UserCreationForm):
# 지금 상태에서는 Custom이나 UserCreationForm이나 다를것 이 없다.
    class Meta:
        model = get_user_model()
        fields = {'username', 'password1', 'password2', 'phone'}

# django에서는 user에 대한 기능을 자동화 해놓은 경우가 많다.
# 이것을 편하게하기 위해 settings에 AUTH_USER_MODEL = 'accounts.User' 이렇게 설정을 해두었다.
# 변수로 쓴다면, 유지보수 하기가 쉬워진다.
# 장고 커스터마이징을 할때에는 이 user를 그대로 쓸 수 있는데.
