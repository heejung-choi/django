from django import forms
from .models import Article, Comment


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content',]
        # 
        #tuple -> ()
        # list -> []
        #fields = '__all__'
        # exclude = 
