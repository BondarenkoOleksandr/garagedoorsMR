from rest_framework import serializers
from taggit.models import Tag

from articles.models import Article, ArticleView, ArticleRating, Comment, SEOArticle, Paragraphs


class SEOArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEOArticle
        exclude = ['article']


class ArticleRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleRating
        fields = '__all__'


class ParagraphsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraphs
        exclude = ['article', 'id']


class ArticleBaseSerializer(serializers.ModelSerializer):
    rating = serializers.CharField()
    count_votes = serializers.CharField()
    comments_count = serializers.CharField()
    views_count = serializers.CharField()
    publish_date = serializers.DateField(format="%d %b %Y")
    bg_image = serializers.ImageField(source='bg_image.image', allow_null=True)
    bg_image__alt = serializers.CharField(source='bg_image.alt', allow_null=True)
    bg_image__title = serializers.CharField(source='bg_image.title', allow_null=True)
    author__first_name = serializers.CharField(source='author.first_name')
    author__last_name = serializers.CharField(source='author.last_name')
    seo = SEOArticleSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(ArticleBaseSerializer):
    pass


class ArticleDetailSerializer(ArticleBaseSerializer):
    paragraphs = ParagraphsSerializer(many=True)


class ArticleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleView
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='user.profile.image', allow_null=True)
    pub_date = serializers.DateField(format="%d %b %Y")
    user__first_name = serializers.CharField(source='user.first_name')
    user__last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Comment
        exclude = ['article', 'status']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
