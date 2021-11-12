from django.contrib import admin

# Register your models here.
from nested_inline.admin import NestedStackedInline

from services.models import Service, ServiceCategory, ServiceArticle, ServiceReview, SEOService


class ServiceReviewInline(admin.StackedInline):
    model = ServiceReview


class SEOServiceInlines(admin.StackedInline):
    model = SEOService


class ServiceArticleInlines(admin.StackedInline):
    model = ServiceArticle


class ServiceAdmin(admin.ModelAdmin):
    inlines = (ServiceArticleInlines, ServiceReviewInline, SEOServiceInlines)
    search_fields = ['category__name', 'name']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory)
