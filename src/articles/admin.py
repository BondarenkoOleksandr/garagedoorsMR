from django.contrib import admin

from articles.forms import ArticleForm
from articles.models import Article, Paragraphs, Comment, ArticleRating, SEOArticle


class ArticleInlines(admin.StackedInline):
    model = Paragraphs


class ArticleRatingInlines(admin.StackedInline):
    model = ArticleRating


class SEOArticleInlines(admin.StackedInline):
    model = SEOArticle


class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleInlines, ArticleRatingInlines, SEOArticleInlines)
    search_fields = ['title']
    form = ArticleForm


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
