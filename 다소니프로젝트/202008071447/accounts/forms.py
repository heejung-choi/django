from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('name_kr', 'phone', )



class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(
        label='핸드폰 번호',
        widget=forms.TextInput(
            attrs={
                'type':'tel',
            }
        )
    )
    username = forms.CharField(
        label='아이디',
        help_text='문자, 숫자 그리고 @/./+/-/_만 가능합니다.'
    )
    name_kr = forms.CharField(
        label='이름'
    )


    class Meta():
        model = get_user_model()
        fields = ('username', 'password1', 'password2','name_kr', 'phone')
        #fields = '__all__'

