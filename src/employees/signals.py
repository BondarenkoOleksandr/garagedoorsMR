from autoslug.utils import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

from employees.models import Employee


@receiver(post_save, sender=Employee)
def save_employee(sender, instance, created, **kwargs):

    if created:
        value = instance.name
        instance.slug = slugify(value)
        instance.save()
