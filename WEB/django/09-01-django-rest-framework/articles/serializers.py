from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)