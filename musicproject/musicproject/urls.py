"""musicprojekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from store import views as store
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from store import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    url(r'^$', store.home, name="home"),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^store$', store.store, name="store"),
    url(r'^news/(?P<slug>[\w\-_]+)/$', store.news_detail, name='news-detail'),
    url(r'^albums/(?P<slug>[\w\-_]+)/$', store.album_detail, name='album-detail'),
    url(r'^albums$', store.albums_list, name="albums_list"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^news/(?P<slug>[\w\-_]+)/comment/$', views.add_comment_to_news, name='add_comment_to_news'),
    url(r'^albums/(?P<slug>[\w\-_]+)/comment/$', views.add_comment_to_album, name='add_comment_to_album'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^album/comment/(?P<pk>\d+)/approve/$', views.album_comment_approve, name='album_comment_approve'),
    url(r'^album/comment/(?P<pk>\d+)/remove/$', views.album_comment_remove, name='album_comment_remove'),
    url(r'^add/news/$', views.add_news, name='add_news'),
    url(r'^add/album/$', views.add_album, name='add_album'),
    url(r'^edit/album/(?P<slug>[\w\-_]+)/$', store.edit_album, name='edit_album'),
    url(r'^edit/news/(?P<slug>[\w\-_]+)/$', store.edit_news, name='edit_news'),
    url(r'^delete/news/(?P<slug>[\w\-_]+)/$', store.delete_news, name='delete_news'),
    url(r'^delete/albums/(?P<slug>[\w\-_]+)/$', store.delete_album, name='delete_album')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
