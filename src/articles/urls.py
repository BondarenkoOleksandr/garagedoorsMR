from django.urls import path

from articles.views import ArticleListView, ArticleDetailView

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='single'),
]
