from django.db import models

# Create your models here.


class City(models.Model):
    state = models.ForeignKey(to='cities.State', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
