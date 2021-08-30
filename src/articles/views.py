from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'
    pk_url_kwarg = 'id'
