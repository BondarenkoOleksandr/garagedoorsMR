# Generated by Django 3.2.6 on 2021-10-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_seoemployee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seoemployee',
            options={'verbose_name_plural': 'SEO'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=1, null=True),
        ),
    ]
