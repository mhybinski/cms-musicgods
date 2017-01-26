# Register your models here.
from django.contrib import admin
from .models import Album, News, NewsComment, AlbumsComment


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'genre')
    list_display_links = ('artist', 'title', 'genre')
    list_per_page = 25

admin.site.register(Album, AlbumAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_display_links = ('title', 'author', 'published_date')
    list_per_page = 25

class NewsCommentsAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'approved_comment')
    list_display_links = ('post', 'author', 'approved_comment')
    list_per_page = 25

class AlbumsCommentsAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'approved_comment')
    list_display_links = ('post', 'author', 'approved_comment')
    list_per_page = 25

admin.site.register(News, NewsAdmin)
admin.site.register(NewsComment, NewsCommentsAdmin)
admin.site.register(AlbumsComment, AlbumsCommentsAdmin)