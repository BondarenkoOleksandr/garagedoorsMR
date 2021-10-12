from django.contrib import admin

from articles.models import Article, Paragraphs, Comment, ArticleRating, SEOArticle


class ArticleInlines(admin.StackedInline):
    model = Paragraphs


class SEOArticleInlines(admin.StackedInline):
    model = SEOArticle


class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleInlines, SEOArticleInlines)
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
