# Generated by Django 3.2.6 on 2021-08-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_articleviews_articleview'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
