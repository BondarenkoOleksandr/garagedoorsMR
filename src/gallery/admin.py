from django.contrib import admin

# Register your models here.
from gallery.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    fields = ('image_tag', 'image', 'alt', 'title', )
    readonly_fields = ('image_tag',)
    list_display = ('image_tag', 'alt', 'title')
    list_per_page = 10
    search_fields = ('alt', 'title')


admin.site.register(Photo, PhotoAdmin)
