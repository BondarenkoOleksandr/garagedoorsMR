from django.contrib import admin

# Register your models here.
from services.models import Service, ServiceCategory

class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['category__name']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory)
