# Generated by Django 3.2.6 on 2021-10-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SEOBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(blank=True, max_length=500, null=True)),
                ('seo_description', models.TextField(blank=True, max_length=500, null=True)),
                ('seo_canonical', models.URLField(blank=True, null=True)),
                ('seo_robots', models.CharField(blank=True, max_length=500, null=True)),
                ('seo_schema', models.TextField(blank=True, null=True)),
                ('seo_og', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'SEO',
            },
        ),
    ]
