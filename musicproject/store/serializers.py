from django.contrib.auth.models import User, Group
from models import Album, News
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        permission_classes = [IsAuthenticatedOrReadOnly]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('artist','title', 'genre','review')

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('title','author', 'published_date','summary','content')