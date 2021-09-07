from django.db import models

# Create your models here.
from services.models import Service


class FAQ(models.Model):
    service = models.ForeignKey(to=Service, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
