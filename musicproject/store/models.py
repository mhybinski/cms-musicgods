from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="",allow_unicode=True,max_length=255)
    author = models.ForeignKey(User)
    published_date = models.DateField(default=timezone.now)
    image = models.FileField(blank=True, null=True)
    summary = models.CharField(max_length=500)
    content = RichTextField()

    def __unicode__(self):
        return u'%s %s' % (self.title, self.author)

class NewsComment(models.Model):
    post = models.ForeignKey(News, related_name='comments')
    author = models.ForeignKey(User)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Album(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="", allow_unicode=True, max_length=255)
    cover = models.FileField(blank=True, null=True)
    released_date = models.DateField(default=timezone.now)
    genre = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    review = RichTextField()
    review_author = models.ForeignKey(User)
    RATE_CHOICES = [(r, r) for r in range(0, 6)]
    rating = models.IntegerField(('rate'), max_length=1, choices=RATE_CHOICES, default=3)

    def __unicode__(self):
        return u'%s %s' % (self.title, self.artist)

class AlbumsComment(models.Model):
    post = models.ForeignKey(Album, related_name='comments')
    author = models.ForeignKey(User)
    RATE_CHOICES = [(r, r) for r in range(0, 6)]
    rating = models.IntegerField(('rate'), max_length=1, choices=RATE_CHOICES, default=3)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text