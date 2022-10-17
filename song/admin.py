from django.contrib import admin
from song.models import Song,User,Like
# Register your models here.
class Data(admin.ModelAdmin):
    list_display=('title','artist','image','audio_file','audio_link','durations')

class Data2(admin.ModelAdmin):
    list_display=('id','username','password','is_authenticated')

class Data3(admin.ModelAdmin):
    list_display=('user_id','song_title','is_like')

admin.site.register(Song,Data)
admin.site.register(User,Data2)
admin.site.register(Like,Data3)