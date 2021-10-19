from django.contrib.auth.models import User
from django.db.models import Avg, Count
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404, CreateAPIView

from taggit.models import Tag
from articles.api.serializers import ArticleListSerializer, TagSerializer, CommentSerializer, ArticleRatingSerializer, ArticleDetailSerializer
from articles.models import Article, Comment, ArticleRating
from core.utils import get_user_ip, get_user_by_jwt, LargeResultsSetPagination


class ArticleListView(ListAPIView):
    serializer_class = ArticleListSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return self.queryset.annotate(rating=Avg('article_rating__rating'), count_votes=Count('article_rating'),
                                      comments_count=Count('comments'), views_count=Count('articleview'))


class TagsListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.values('name', 'slug')


class ArticleCommentListView(ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return Comment.objects.filter(article__id=self.kwargs['id'], status=1)


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.annotate(rating=Avg('article_rating__rating'), count_votes=Count('article_rating'),
                                      comments_count=Count('comments'), views_count=Count('articleview'))


class ArticleDetailBySlugView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.annotate(rating=Avg('article_rating__rating'), count_votes=Count('article_rating'),
                                      comments_count=Count('comments'), views_count=Count('articleview'))


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


class ArticleByTagView(ListAPIView):
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        search_tags = self.request.data.get('tags', '').lower().split(',')
        queryset = Article.objects.filter(tags__slug__in=search_tags).distinct()
        return queryset.annotate(rating=Avg('article_rating__rating'), count_votes=Count('article_rating'),
                                 comments_count=Count('comments'), views_count=Count('articleview'))


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
