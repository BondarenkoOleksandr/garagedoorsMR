from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='services/single')
    slug = models.SlugField()
    category = models.ForeignKey(to='services.ServiceCategory', on_delete=models.SET_NULL, null=True)
    excerpt = models.TextField(max_length=500)

    def __str__(self):
        return self.name + ' - ' + self.category.name


class ServiceCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
