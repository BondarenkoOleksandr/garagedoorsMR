import json

from django.http import JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.generics import ListAPIView
from taggit.models import Tag

from articles.api.serializers import ArticleSerializer, TagSerializer, CommentSerializer
from articles.models import Article, Comment


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        comments = Comment.objects.filter(article__id=article_id, status=1)
        articles = Article.objects.values('author__username', 'title', 'excerpt', 'image', 'publish_date', 'slug')
        articles = json.dumps(list(articles), cls=DjangoJSONEncoder)

        data = {"articles": articles}

        return JsonResponse(data)


class TagsListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, id):
        article_id = id
        comments = Comment.objects.filter(article__id=article_id, status=1)
        if comments:
            comments = serializers.serialize("json", comments)
            data = {"comments": comments}
            return JsonResponse(data)
        else:
            return JsonResponse({'empty': 1})
