# Generated by Django 3.2.6 on 2021-09-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0006_auto_20210902_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thirdscreen',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='states/third_screen/'),
        ),
    ]