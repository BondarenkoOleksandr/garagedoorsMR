# Generated by Django 3.2.6 on 2021-10-01 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0014_alter_city_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(default='<function uuid1 at 0x7fd30fdeeca0><function uuid3 at 0x7fd30fdeed30>', editable=False, max_length=150, unique=True),
        ),
    ]
