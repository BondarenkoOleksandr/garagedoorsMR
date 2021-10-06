import uuid

from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError


class Service(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='services/single')
    slug = models.SlugField(
        max_length=250,
        editable=False,
        unique=True
    )
    category = models.ForeignKey(to='services.ServiceCategory', on_delete=models.SET_NULL, null=True)
    excerpt = models.TextField(max_length=500)

    def clean(self):
        if not self.slug and Service.objects.filter(name__iexact=self.name, category=self.category):
            raise ValidationError('Service with this name and category already exists')

    def __str__(self):
        return self.name + ' - ' + self.category.name


class ServiceCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        editable=False,
        unique=True
    )

    def clean(self):
        if not self.slug and ServiceCategory.objects.filter(name__iexact=self.name):
            raise ValidationError('Service category with this name already exists')


    class Meta:
        verbose_name_plural = "Service categories"

    def __str__(self):
        return self.name


class ServiceArticle(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    article = models.OneToOneField(Service, null=True, on_delete=models.SET_NULL)
    subtitle = models.CharField(max_length=200)
    text = models.TextField()
