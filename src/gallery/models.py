from django.db import models

# Create your models here.


class Photo(models.Model):
    image = models.ImageField(upload_to='gallery')
    alt = models.CharField(max_length=250)
    title = models.CharField(max_length=250)

    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape(self.image.url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
