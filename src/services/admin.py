from django.contrib import admin

# Register your models here.
from services.models import Service, ServiceCategory, ServiceArticle, ServiceReview


class ServiceInlines(admin.TabularInline):
    model = ServiceArticle


class ServiceReviewInline(admin.TabularInline):
    model = ServiceReview


class ServiceAdmin(admin.ModelAdmin):
    inlines = (ServiceInlines, ServiceReviewInline)
    search_fields = ['category__name']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory)
