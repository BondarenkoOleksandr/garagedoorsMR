from PIL import Image
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(default='user.png', upload_to='users/', null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.image)
        image.thumbnail((300, 300), Image.ANTIALIAS)
        image.save(self.image.path)

    def __str__(self):
        return self.user.username
