import uuid

from django.db import models

# Create your models here.
from states.models import State


class Employee(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='employees/', null=True)
    position = models.CharField(max_length=100)
    type_of_works = models.TextField()
    state = models.ForeignKey(to=State, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(
        max_length=150,
        editable=False,
        default=uuid.uuid1
    )
    def __str__(self):
        return self.name + ' - ' + self.position


class Review(models.Model):
    STARS = (
        (1, 'Very bad'),
        (2, 'Bad'),
        (3, 'Normal'),
        (4, 'Good'),
        (5, 'Excellent'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    pub_date = models.DateField()
    text = models.TextField()
    rating = models.IntegerField(choices=STARS, default=STARS[4])

    def __str__(self):
        return self.name + ' - ' + self.text[:35] + self.employee.name
