from django.contrib import admin

# Register your models here.
from services.models import Service, ServiceCategory, ServiceArticle


class ServiceInlines(admin.TabularInline):
    model = ServiceArticle

class ServiceAdmin(admin.ModelAdmin):
    inlines = (ServiceInlines, )
    search_fields = ['category__name']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory)
