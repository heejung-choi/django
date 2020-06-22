from django.contrib import admin
from .models import Movie, Comment

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'title_en', 'audience', 'open_date','genre', 'watch_grade', 'score', 'poster_url']
    list_editable = ['title']    

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)
# admin site에 등록(register) 하겠다.