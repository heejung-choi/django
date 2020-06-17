from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title.',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'cols': 50,
                'rows': 5,
            }
        )
    )

    # Meta - ArticleForm 클래스에 대한 정보를 작성하는 곳
    class Meta:
        model = Article
        # fields = ['title', 'content',]
        fields = '__all__'
        # exclude = ['title'] 