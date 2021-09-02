# Generated by Django 3.2.6 on 2021-09-02 10:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0029_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=uuid.UUID('7ad25d38-0bda-11ec-a981-e4a8df898f19'), editable=False, max_length=100, unique=True),
        ),
    ]
