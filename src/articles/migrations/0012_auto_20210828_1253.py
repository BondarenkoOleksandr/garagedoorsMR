# Generated by Django 3.2.6 on 2021-08-28 09:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20210828_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=uuid.UUID('c19bb744-07e5-11ec-8418-e4a8df898f19'), editable=False, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='articlerating',
            name='rating',
            field=models.SmallIntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Normal'), (4, 'Good'), (5, 'Excellent')], default=(1, 'Very bad'), null=True),
        ),
    ]
