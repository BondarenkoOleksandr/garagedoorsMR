from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='employees/', null=True)
    position = models.CharField(max_length=100)
    type_of_works = models.TextField()
    state = models.OneToOneField(to='employees.State', on_delete=models.SET_NULL, null=True)


class State(models.Model):
    name = models.CharField(max_length=100)
