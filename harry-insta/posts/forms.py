from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'content',
            'image',
        ]


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
    )

    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        # fields = '__all__'
