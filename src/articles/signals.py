from autoslug.utils import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

from articles.models import Article


@receiver(post_save, sender=Article)
def save_lesson(sender, instance, created, **kwargs):
    if created:
        value = instance.title
        instance.slug = slugify(value)
        instance.save()
