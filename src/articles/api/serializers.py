from rest_framework import serializers
from taggit.models import Tag

from articles.models import Article, ArticleView, ArticleRating, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleView
        fields = '__all__'


class ArticleRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleRating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
