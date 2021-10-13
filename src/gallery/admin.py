from django.contrib import admin

# Register your models here.
from gallery.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    fields = ('image_tag', 'alt', 'title', )
    readonly_fields = ('image_tag',)


admin.site.register(Photo, PhotoAdmin)
