# Generated by Django 3.2.6 on 2021-10-13 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0010_alter_seostate_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstscreen',
            name='image',
        ),
        migrations.RemoveField(
            model_name='thirdscreen',
            name='image',
        ),
    ]
