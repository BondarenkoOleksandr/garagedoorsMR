from django.db import models

# Create your models here.


class Photo(models.Model):
    image = models.ImageField(upload_to='gallery')
    alt = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
