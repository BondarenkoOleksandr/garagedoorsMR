from django.contrib import admin

from articles.models import Article, Paragraphs, Comment


class ArticleInlines(admin.TabularInline):
    model = Paragraphs


class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleInlines,)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
