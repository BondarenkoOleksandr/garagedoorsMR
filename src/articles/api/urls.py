from django.urls import path

from articles.api.views import ArticleListView, TagsListView, CommentListView

app_name = 'articles_api'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles-list'),
    path('tags/', TagsListView.as_view(), name='articles-list'),
    path('get_comments/<int:id>/', CommentListView.as_view(), name='article-get-comments'),
]
