# Generated by Django 3.2.6 on 2021-08-27 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210827_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraphs',
            name='image',
            field=models.ImageField(null=True, upload_to='articles/par/'),
        ),
    ]
