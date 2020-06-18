from django import forms
from .models import Movie

# title = models.CharField(max_length=50)
# title_en = models.CharField(max_length=50)
# audience = models.IntegerField(default=0)
# open_date = models.DateTimeField()
# genre = models.CharField(max_length=50)
# watch_grade = models.CharField(max_length=50)
# score = models.FloatField()
# poster_url = models.TextField()
# descripthon = models.TextField()

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='영화명',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': '영화명을 입력하세요.',
            }
        )
    )

    title_en = forms.CharField(
        label='영화명(영문)',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title_en form-control',
                'placeholder': '영화명(영문)을 입력하세요.',
            }
        )
    )

    audience = forms.IntegerField(
        label='누적 관객수',
        widget=forms.NumberInput(
            attrs={
                'class': 'my-audience form-control',
                'placeholder': '누적관객수를 입력하세요.',
            }
        )
    )
    
    open_date = forms.DateTimeField(
        label='개봉일',
        widget=forms.DateTimeInput(
             attrs={
                'class': 'my-open_date form-control',
                'placeholder': '개봉일을 입력하세요.',
            }
        )
    )

    genre = forms.CharField(
        label='장르',
        widget=forms.TextInput(
            attrs={
                'class': 'my-genre form-control',
                'placeholder': '장르를 입력하세요.',
            }
        )
    )
    
    watch_grade = forms.CharField(
        label='관람등급',
        widget=forms.TextInput(
            attrs={
                'class': 'my-watch_grade form-control',
                'placeholder': '관람등급을 입력하세요.',
            }
        )
    )

    score = forms.FloatField(
        label='평점',
        widget=forms.NumberInput(
            attrs={
                'class': 'my-score form-control',
                'placeholder': '평점을 입력하세요.',
            }
        )
    )

    poster_url = forms.CharField(
        label='포스터 이미지 URL',
        widget=forms.Textarea(
            attrs={
                'class': 'my-poster_url form-control',
                'placeholder': '포스터 이미지 URL을 입력하세요.',
            }
        )
    )

    descripthon = forms.CharField(
        label='영화 소개',
        widget=forms.Textarea(
            attrs={
                'class': 'my-descripthon form-control',
                'placeholder': '영화 소개를 입력하세요.',
            }
        )
    )    
    
    class Meta:
        model = Movie        
        fields = '__all__'
 