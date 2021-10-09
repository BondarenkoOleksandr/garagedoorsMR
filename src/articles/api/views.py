import datetime
import json

from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from requests import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404, CreateAPIView
from taggit.models import Tag
from django.forms.models import model_to_dict

from accounts.models import UserProfile
from app.settings import base
from articles.api.serializers import ArticleSerializer, TagSerializer, CommentSerializer, ArticleRatingSerializer
from articles.models import Article, Comment, ArticleRating, ArticleView, Paragraphs
from core.utils import get_user_ip, queryset_pagination, get_user_by_jwt


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        articles = Article.objects.all()
        articles = Article.objects.values('id', 'author__first_name', 'author__last_name', 'title', 'excerpt', 'image',
                                          'publish_date',
                                          'slug')

        articles = queryset_pagination(request, articles)
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
                            'image': request.scheme + '://' + request.get_host() + '/' + base.MEDIA_URL + article[
                                'image'],
                            })
            if article['publish_date']:
                article.update({'publish_date': article['publish_date'].strftime("%d %b %Y")})
            indx += 1

        data = list(articles)

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


class TagsListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.values('name', 'slug')


class ArticleCommentListView(ListAPIView):
    serializer_class = CommentSerializer

    def get(self, request, id):
        comments = Comment.objects.filter(article__id=id, status=1).values('id', 'user__first_name', 'user__id', 'user__last_name', 'parent__id', 'text')
        comments = queryset_pagination(self.request, comments)
        for comment in comments:
            user = UserProfile.objects.get(user__id=comment.pop('user__id'))
            comment.update({'image': request.scheme + '://' + request.get_host() + user.image.url})
        
        return JsonResponse(list(comments), safe=False, json_dumps_params={'indent': 2})


class ArticleDetailView(RetrieveAPIView):
    serializer_class = ArticleSerializer

    def get(self, request, id):
        article = Article.objects.filter(id=id)
        if not article:
            return JsonResponse(['Article not fount'], safe=False)
        tags_list = list(article.first().tags.values('name'))
        obj, created = ArticleView.objects.get_or_create(IPAddress=get_user_ip(request), article=article.first())
        article = article.values('id', 'author__first_name', 'author__last_name', 'title', 'excerpt', 'image',
                                 'publish_date', 'slug')

        article = queryset_pagination(request, article)

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
                        'tags': tags_list,
                        'image': request.scheme + '://' + request.get_host() + '/' + base.MEDIA_URL + art['image'],
                        'paragraphs': paragr})
            if art['publish_date']:
                art.update({'publish_date': art['publish_date'].strftime("%d %b %Y")})

        data = list(article)

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


class ArticleDetailBySlugView(RetrieveAPIView):
    serializer_class = ArticleSerializer

    def get(self, request, slug):
        article = Article.objects.filter(slug=slug)
        tags_list = list(article.first().tags.values('name', 'slug'))
        if not article:
            return JsonResponse(['Article not fount'], safe=False)
        obj, created = ArticleView.objects.get_or_create(IPAddress=get_user_ip(request), article=article.first())
        article = article.values('id', 'author__first_name', 'author__last_name', 'title', 'excerpt', 'image',
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
                        'tags': tags_list,
                        'image': request.scheme + '://' + request.get_host() + '/' + base.MEDIA_URL + art['image'],
                        'paragraphs': paragr})

            if art['publish_date']:
                art.update({'publish_date': art['publish_date'].strftime("%d %b %Y")})

        try:
            article.first().update({'image': request.get_host() + base.MEDIA_URL + art['image']})
        except:
            article.first().update({'image': None})

        data = list(article)

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


class ArticleRatingCreateView(CreateAPIView):
    queryset = ArticleRating.objects.all()
    serializer_class = ArticleRatingSerializer

    def post(self, request):
        article_id = request.POST.get('article', '')
        rating = self.request.POST.get('rating', 5)
        if not article_id or not rating:
            return HttpResponseBadRequest('Mandatory data not transmitted', status=400)
        article = get_object_or_404(Article, id=article_id)
        obj, created = ArticleRating.objects.get_or_create(IPAddress=get_user_ip(request), article=article)
        if obj:
            obj.rating = rating
            obj.save()

        return JsonResponse({'success': 1, 'rating': obj.rating})


class ArticleByTagView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        search_tags = self.request.GET.get('tags', '').lower().split(',')
        articles_by_tag = Article.objects.filter(tags__slug__in=search_tags).distinct()
        tags_list = [list(obj.tags.values('name', 'slug')) for obj in articles_by_tag]
        articles_by_tag = articles_by_tag.values('id', 'author__first_name', 'author__last_name', 'title', 'excerpt',
                                                 'image', 'publish_date', 'slug')
        articles_by_tag = queryset_pagination(request, articles_by_tag)
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
                 'image': request.scheme + '://' + request.get_host() + '/' + base.MEDIA_URL + article['image'],
                 })

            if article['publish_date']:
                article.update({'publish_date': article['publish_date'].strftime("%d %b %Y")})

            indx += 1

        data = list(articles_by_tag)

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


class CreateCommentAPI(CreateAPIView):

    def post(self, request, *args, **kwargs):
        article_id = request.data.get('article', '')
        text = request.data.get('text', '')
        parent = request.data.get('parent', '')

        user = get_user_by_jwt(request)
        article = get_object_or_404(Article, id=article_id)

        if isinstance(user, User):

            comment = Comment.objects.create(
                user=user,
                article=article,
                text=text,
            )

            if parent:
                parent = get_object_or_404(Comment, id=parent)
                comment.parent = parent
                comment.save()

            return JsonResponse({'status': 1})

        else:
            return JsonResponse(user[0], status=400, safe=False)
