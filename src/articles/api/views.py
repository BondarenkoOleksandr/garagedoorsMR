import json

from django.db.models import Avg
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from requests import Response
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
        articles = Article.objects.all()
        tags_list = [list(article.tags.values('name')) for article in articles]
        articles = Article.objects.values('id', 'author__username', 'title', 'excerpt', 'image', 'publish_date',
                                          'slug')
        indx = 0
        for article in articles:
            article.update({'comments_count': Comment.objects.filter(article__id=article['id'], status=1).count(),
                            'views_count': ArticleView.objects.filter(IPAddress=get_user_ip(request),
                                                                      article__id=article['id']).count(),
                            'rating': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                                   article__id=article['id']).aggregate(
                                Avg('rating')),
                            'count_votes': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                                        article__id=article['id']).count(),
                            'tags': tags_list[indx]
                            })
            indx+=1

        data = list(articles)

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


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
        if not article:
            return JsonResponse(['Article not fount'], safe=False)
        obj, created = ArticleView.objects.get_or_create(IPAddress=get_user_ip(request), article=article.first())
        article = article.values('id', 'author__username', 'title', 'excerpt', 'image',
                                 'publish_date', 'slug')

        for art in article:
            paragr = []
            for model in Paragraphs.objects.filter(article__id=id):
                dict_model = model_to_dict(model, fields=['title', 'text', 'quote'])
                try:
                    dict_model.update({'image': request.build_absolute_uri(model.image.url)})
                except:
                    dict_model.update({'image': None})
                paragr.append(dict_model)
            art.update({'comments_count': Comment.objects.filter(article__id=id, status=1).count(),
                        'views_count': ArticleView.objects.filter(IPAddress=get_user_ip(request),
                                                                  article__id=id).count(),
                        'rating': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                               article__id=id).aggregate(Avg('rating')),
                        'count_votes': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                                    article__id=id).count(),
                        'tags': list(art.tags.values('name')),
                        'paragraphs': paragr})

        try:
            article.first().update({'image': request.build_absolute_uri(article.first()['image'])})
        except:
            article.first().update({'image': None})

        data = article

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


class ArticleDetailBySlugView(RetrieveAPIView):
    serializer_class = ArticleSerializer

    def get(self, request, slug):
        article = Article.objects.filter(slug=slug)
        if not article:
            return JsonResponse(['Article not fount'], safe=False)
        obj, created = ArticleView.objects.get_or_create(IPAddress=get_user_ip(request), article=article.first())
        article = article.values('id', 'author__username', 'title', 'excerpt', 'image',
                                 'publish_date', 'slug')

        for art in article:
            paragr = []
            for model in Paragraphs.objects.filter(article__slug=slug):
                dict_model = model_to_dict(model, fields=['title', 'text', 'quote'])
                try:
                    dict_model.update({'image': request.build_absolute_uri(model.image.url)})
                except:
                    dict_model.update({'image': None})
                paragr.append(dict_model)
            art.update({'comments_count': Comment.objects.filter(article__slug=slug, status=1).count(),
                        'views_count': ArticleView.objects.filter(IPAddress=get_user_ip(request),
                                                                  article__slug=slug).count(),
                        'rating': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                               article__slug=slug).aggregate(Avg('rating')),
                        'count_votes': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                                    article__slug=slug).count(),
                        'tags': list(art.tags.values('name')),
                        'paragraphs': paragr})

        try:
            article.first().update({'image': request.build_absolute_uri(article.first()['image'])})
        except:
            article.first().update({'image': None})

        data = list(article)

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


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


class ArticleByTagView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        search_tags = self.request.GET.get('tags', '').split(',')
        articles_by_tag = Article.objects.filter(tags__name__in=search_tags).distinct()
        tags_list = [list(obj.tags.values('name')) for obj in articles_by_tag]
        articles_by_tag = articles_by_tag.values('id', 'author__username', 'title', 'excerpt', 'image', 'publish_date',
                                          'slug')
        indx = 0
        for article in articles_by_tag:
            article.update(
                {'comments_count': Comment.objects.filter(article__id=article['id'], status=1).count(),
                 'views_count': ArticleView.objects.filter(IPAddress=get_user_ip(request),
                                                           article__id=article['id']).count(),
                 'rating': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                        article__id=article['id']).aggregate(
                     Avg('rating')),
                 'count_votes': ArticleRating.objects.filter(IPAddress=get_user_ip(request),
                                                             article__id=article['id']).count(),
                 'tags': tags_list[indx],
                 })
            indx+=1

        data = list(articles_by_tag)

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})
