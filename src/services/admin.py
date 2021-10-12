from django.contrib import admin

# Register your models here.
from services.models import Service, ServiceCategory, ServiceArticle, ServiceReview, SEOServiceArticle


class ServiceInlines(admin.StackedInline):
    model = ServiceArticle


class ServiceReviewInline(admin.StackedInline):
    model = ServiceReview


class SEOServiceArticleInlines(admin.StackedInline):
    model = SEOServiceArticle


class ServiceAdmin(admin.ModelAdmin):
    inlines = (ServiceInlines, ServiceReviewInline)
    search_fields = ['category__name', 'name']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory)
