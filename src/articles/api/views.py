import json

from django.db.models import Avg
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404, CreateAPIView
from taggit.models import Tag
from django.forms.models import model_to_dict
from articles.api.serializers import ArticleSerializer, TagSerializer, CommentSerializer, ArticleRatingSerializer
from articles.models import Article, Comment, ArticleRating, ArticleView, Paragraphs
from core.utils import get_user_ip


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        articles = Article.objects.values('id', 'author__username', 'title', 'excerpt', 'image', 'publish_date', 'slug')
        for article in articles:
            article.update({'comments_count': Comment.objects.filter(article__id=article['id'], status=1).count(),
                            'views_count': ArticleView.objects.filter(IPAddress=get_user_ip(request),
                                                                      article__id=article['id']).count(),
                            'rating': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                                   article__id=article['id']).aggregate(Avg('rating')),
                            'count_votes': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                                        article__id=article['id']).count()
                            })
        articles = json.dumps(list(articles), cls=DjangoJSONEncoder)

        data = {"articles": articles}

        return JsonResponse(data)


class TagsListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleCommentListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self, id):
        article_id = id
        return Comment.objects.filter(article__id=article_id, status=1)


class ArticleDetailView(RetrieveAPIView):
    serializer_class = ArticleSerializer

    def get(self, request, id):
        article = Article.objects.filter(id=id)
        obj, created = ArticleView.objects.get_or_create(IPAddress=get_user_ip(request), article=article.first())
        article = article.values('id', 'author__username', 'title', 'excerpt', 'image',
                                 'publish_date', 'slug')
        for art in article:
            print(id)
            paragr = [model_to_dict(model, fields=['title', 'text', 'quote', 'image__url']) for model in
                      Paragraphs.objects.filter(article__id=id)]
            print(paragr)
            art.update({'comments_count': Comment.objects.filter(article__id=id, status=1).count(),
                        'views_count': ArticleView.objects.filter(IPAddress=get_user_ip(request),
                                                                  article__id=id).count(),
                        'rating': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                                  article__id=id).aggregate(Avg('rating')),
                        'count_votes': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                                  article__id=id).count(),
                        'paragraphs': paragr})
        article = json.dumps(list(article), cls=DjangoJSONEncoder)

        data = {"article": article}

        return JsonResponse(data)


class ArticleRatingCreateView(CreateAPIView):
    queryset = ArticleRating.objects.all()
    serializer_class = ArticleRatingSerializer

    def post(self, request, id):
        article = Article.objects.get(id=id)
        rating = self.request.POST.get('rating', 5)
        obj, created = ArticleRating.objects.get_or_create(IPAddress=get_user_ip(request), article=article)
        if obj:
            obj.rating = rating
            obj.save()

        return JsonResponse({'success': 1, 'rating': obj.rating})
