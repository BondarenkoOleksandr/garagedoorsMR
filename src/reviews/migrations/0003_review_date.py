# Generated by Django 3.2.6 on 2021-10-05 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
