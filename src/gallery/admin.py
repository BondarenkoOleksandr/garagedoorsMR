from django.contrib import admin

# Register your models here.
from gallery.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    fields = ('image_tag', 'image', 'alt', 'title', )


admin.site.register(Photo, PhotoAdmin)
