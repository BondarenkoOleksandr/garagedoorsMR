from django.contrib import admin

# Register your models here.
from services.models import Service, ServiceCategory, ServiceArticle, ServiceReview, SEOServiceArticle


class ServiceReviewInline(admin.StackedInline):
    model = ServiceReview


class SEOServiceArticleInlines(admin.StackedInline):
    model = SEOServiceArticle


class ServiceArticleAdmin(admin.ModelAdmin):
    inlines = (SEOServiceArticleInlines, )
    model = ServiceArticle


class ServiceAdmin(admin.ModelAdmin):
    inlines = (ServiceReviewInline, )
    search_fields = ['category__name', 'name']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceArticle, ServiceArticleAdmin)
admin.site.register(ServiceCategory)
