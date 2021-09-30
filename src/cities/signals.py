from autoslug.utils import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

from cities.models import City


@receiver(post_save, sender=City)
def save_city(sender, instance, created, **kwargs):

    if created:
        value = instance.title
        instance.slug = slugify(value)
        instance.save()
