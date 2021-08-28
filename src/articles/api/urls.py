from django.urls import path


from articles.api.views import ArticleListView, TagsListView, ArticleCommentListView, ArticleDetailView

app_name = 'articles_api'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles-list'),
    path('articles/<int:id>/', ArticleDetailView.as_view(), name='single-article'),
    path('tags/', TagsListView.as_view(), name='articles-list'),
    path('get_comments/<int:id>/', ArticleCommentListView.as_view(), name='article-get-comments'),
]
