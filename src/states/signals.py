from autoslug.utils import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

from states.models import State


@receiver(post_save, sender=State)
def save_state(sender, instance, created, **kwargs):

    if created:
        value = instance.name
        instance.slug = slugify(value)
        instance.save()
