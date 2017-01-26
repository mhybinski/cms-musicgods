from django import forms
from store.models import NewsComment, AlbumsComment, News, Album


class NewsCommentForm(forms.ModelForm):

    class Meta:
        model = NewsComment
        fields = ('text',)


class AlbumsCommentForm(forms.ModelForm):

    class Meta:
        model = AlbumsComment
        fields = ('rating' ,'text')


class AddNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'slug', 'published_date', 'image', 'summary', 'content')


class AddAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('artist', 'title', 'slug', 'cover', 'released_date', 'genre', 'length', 'producer', 'review', 'rating')