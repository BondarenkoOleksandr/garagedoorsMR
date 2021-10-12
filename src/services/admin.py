from django.contrib import admin

# Register your models here.
from nested_inline.admin import NestedStackedInline

from services.models import Service, ServiceCategory, ServiceArticle, ServiceReview, SEOServiceArticle


class ServiceReviewInline(admin.StackedInline):
    model = ServiceReview


class SEOServiceInlines(NestedStackedInline):
    model = SEOServiceArticle


class ServiceArticleInlines(NestedStackedInline):
    model = ServiceArticle
    inlines = (SEOServiceInlines, )


class ServiceAdmin(admin.ModelAdmin):
    inlines = (ServiceArticleInlines, ServiceReviewInline)
    search_fields = ['category__name', 'name']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory)
