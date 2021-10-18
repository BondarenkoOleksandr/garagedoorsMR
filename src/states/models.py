import uuid

from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from gallery.models import Photo
from seo.models import SEOBase


class State(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    slug = models.SlugField(
        max_length=150,
        editable=False,
        default=uuid.uuid1
    )

    def __str__(self):
        return self.name

    def clean(self):
        if not self.slug and State.objects.filter(name__iexact=self.name):
            raise ValidationError('State with this title already exists')


class FirstScreen(models.Model):
    state = models.OneToOneField(to=State, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    image = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, related_name='img')

    class Meta:
        verbose_name_plural = "First Screen"


class SecondScreen(models.Model):
    state = models.OneToOneField(to=State, on_delete=models.CASCADE, null=True)
    main_title = models.CharField(max_length=250)
    main_description = models.TextField()
    sec_title = models.CharField(max_length=250)
    sec_description = models.TextField()

    class Meta:
        verbose_name_plural = "Second Screen"


class ThirdScreen(models.Model):
    state = models.OneToOneField(to=State, on_delete=models.CASCADE, blank=True, null=True)
    main_title = models.CharField(max_length=250)
    main_description = models.TextField()
    sec_title = models.CharField(max_length=250)
    sec_description = models.TextField()
    thrd_title = models.CharField(max_length=250)
    thrd_description = models.TextField()
    image = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, related_name='img')

    class Meta:
        verbose_name_plural = "Third Screen"


class Paragraphs(models.Model):
    text = models.TextField(max_length=250)
    state = models.ForeignKey(to='states.State', on_delete=models.CASCADE, related_name='list', null=True)


class SEOState(SEOBase):
    state = models.OneToOneField(State, on_delete=models.CASCADE, null=True, related_name='seo')

    class Meta:
        verbose_name_plural = "SEO"
