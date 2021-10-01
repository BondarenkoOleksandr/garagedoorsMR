# Generated by Django 3.2.6 on 2021-10-01 07:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0007_alter_thirdscreen_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, editable=False, max_length=150),
        ),
    ]
