from django.contrib.auth.decorators import login_required
from django.utils import timezone
from serializers import AlbumSerializer, NewsSerializer
from .models import Album, News, AlbumsComment, NewsComment
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from store import models
from musicproject.forms import NewsCommentForm, AlbumsCommentForm, AddNewsForm, AddAlbumForm
from django.db.models import Q

def home(request):
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    query = request.GET.get("q")
    if query:
        news = News.objects.filter(Q(title__contains=query) |
                                   Q(author__contains=query) |
                                   Q(summary__contains=query)).distinct()
    return render(request, 'base.html', {'news': news})

def albums_list(request):
    albums = Album.objects.filter(released_date__lte=timezone.now()).order_by('released_date')
    query = request.GET.get("q")
    if query:
        albums = Album.objects.filter(Q(title__contains=query) |
                                      Q(genre__contains=query) |
                                      Q(artist__contains=query) |
                                      Q(producer__contains=query)
                                      ).distinct()
    return render(request, 'albums.html', {'albums': albums})

def store(request):
    return render(request, "store/store.html")


class NewsList(generic.ListView):
    model = models.News
    paginate_by = 10
    context_object_name = 'news_list'

news_list = NewsList.as_view()

class NewsDetailView(generic.DetailView):
    model = models.News

news_detail = NewsDetailView.as_view()

class AlbumDetailView(generic.DetailView):
    model = models.Album

album_detail = AlbumDetailView.as_view()


def add_comment_to_news(request, slug):
    post = get_object_or_404(News, slug=slug)
    if request.method == "POST":
        form = NewsCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('news-detail', slug=slug)
    else:
        form = NewsCommentForm()
    return render(request, 'store/add_comment_to_news.html', {'form': form})

def add_comment_to_album(request, slug):
    post = get_object_or_404(Album, slug=slug)
    if request.method == "POST":
        form = AlbumsCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('album-detail', slug=slug)
    else:
        form = AlbumsCommentForm()
    return render(request, 'store/add_comment_to_album.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(NewsComment, pk=pk)
    comment.approve()
    return redirect('news-detail', slug=comment.post.slug)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(NewsComment, pk=pk)
    post_pk = comment.post.slug
    comment.delete()
    return redirect('news-detail', slug=post_pk)


@login_required
def album_comment_approve(request, pk):
    comment = get_object_or_404(AlbumsComment, pk=pk)
    comment.approve()
    return redirect('album-detail', slug=comment.post.slug)

@login_required
def album_comment_remove(request, pk):
    comment = get_object_or_404(AlbumsComment, pk=pk)
    post_pk = comment.post.slug
    comment.delete()
    return redirect('album-detail', slug=post_pk)


def add_news(request):
    if request.method == "POST":
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            newsik = form.save(commit=False)
            newsik.author = request.user
            newsik.save()
            return redirect('home')
    else:
        form = AddNewsForm()
    return render(request, 'store/add_news.html', {'form': form})


def add_album(request):
    if request.method == "POST":
        form = AddAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            albumik = form.save(commit=False)
            albumik.review_author = request.user
            albumik.save()
            return redirect('albums_list')
    else:
        form = AddAlbumForm()
    return render(request, 'store/add_album.html', {'form': form})


def edit_album(request, slug):
    post = get_object_or_404(Album, slug=slug)
    if request.method == "POST":
        form = AddAlbumForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('albums_list')
    else:
        form = AddAlbumForm(instance=post)
    return render(request, 'store/add_album.html', {'form': form})


def edit_news(request, slug):
    post = get_object_or_404(News, slug=slug)
    if request.method == "POST":
        form = AddNewsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = AddNewsForm(instance=post)
    return render(request, 'store/add_news.html', {'form': form})


def delete_news(request, slug):
   post = get_object_or_404(News, slug=slug)
   post.delete()
   return redirect('home')


def delete_album(request, slug):
   post = get_object_or_404(Album, slug=slug)
   post.delete()
   return redirect('albums_list')

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer