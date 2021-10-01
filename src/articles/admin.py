from django.contrib import admin

from articles.models import Article, Paragraphs, Comment, ArticleRating


class ArticleInlines(admin.TabularInline):
    model = Paragraphs


class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleInlines,)
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
