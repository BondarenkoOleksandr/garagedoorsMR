# Generated by Django 3.2.6 on 2021-08-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0002_firstscreen_paragraphs_secondscreen_thirdscreen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstscreen',
            name='image',
            field=models.ImageField(null=True, upload_to='states/first_screen/'),
        ),
        migrations.AlterField(
            model_name='thirdscreen',
            name='image',
            field=models.ImageField(null=True, upload_to='states/third_screen/'),
        ),
    ]
