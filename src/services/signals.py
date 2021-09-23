from autoslug.utils import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

from services.models import Service, ServiceCategory


@receiver(post_save, sender=Service)
def save_lesson(sender, instance, created, **kwargs):
    if created:
        value = instance.name
        instance.slug = slugify(value) + '-' + instance.category.slug
        instance.save()


@receiver(post_save, sender=ServiceCategory)
def save_lesson(sender, instance, created, **kwargs):
    if created:
        value = instance.name
        instance.slug = slugify(value)
        instance.save()
