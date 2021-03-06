import uuid

from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from gallery.models import Photo
from seo.models import SEOBase
from states.models import State


class City(models.Model):
    state = models.ForeignKey(to=State, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    zip = models.IntegerField(null=True)
    is_main = models.BooleanField(default=False)
    is_menu = models.BooleanField(default=False)
    slug = models.SlugField(
        max_length=150,
        editable=False,
        default=uuid.uuid1
    )

    def clean(self):
        if not self.slug and City.objects.filter(name__iexact=self.name):
            raise ValidationError('City with this title already exists')

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class FirstScreen(models.Model):
    city = models.OneToOneField(to=City, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    image = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "First Screen"


class SecondScreen(models.Model):
    city = models.OneToOneField(to=City, on_delete=models.CASCADE, null=True)
    main_title = models.CharField(max_length=250)
    main_description = models.TextField()
    sec_title = models.CharField(max_length=250)
    sec_description = models.TextField()

    class Meta:
        verbose_name_plural = "Second Screen"


class ThirdScreen(models.Model):
    city = models.OneToOneField(to=City, on_delete=models.CASCADE, null=True)
    main_title = models.CharField(max_length=250)
    main_description = models.TextField()
    sec_title = models.CharField(max_length=250)
    sec_description = models.TextField()
    thrd_title = models.CharField(max_length=250)
    thrd_description = models.TextField()
    image = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Third Screen"


class Paragraphs(models.Model):
    text = models.TextField(max_length=250)
    state = models.ForeignKey(to='cities.Paragraphs', on_delete=models.CASCADE, related_name='list', null=True)


class SEOCity(SEOBase):
    state = models.OneToOneField(City, on_delete=models.CASCADE, null=True, related_name='seo')

    class Meta:
        verbose_name_plural = "SEO"
