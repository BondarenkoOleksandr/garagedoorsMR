from django.db import models

# Create your models here.


class Coupon(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.title
