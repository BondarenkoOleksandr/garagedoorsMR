# Generated by Django 3.2.6 on 2021-10-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0016_auto_20211013_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstscreen',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cities/first_screen/'),
        ),
        migrations.AlterField(
            model_name='thirdscreen',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cities/third_screen/'),
        ),
    ]
