from django.db import models
from django.utils.html import mark_safe
# Create your models here.


class Photo(models.Model):
    image = models.ImageField(upload_to='gallery')
    alt = models.CharField(max_length=250)
    title = models.CharField(max_length=250)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" height="300" />' % self.image)

    image_tag.short_description = 'Preview'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title + ' - ' + str(self.id)
