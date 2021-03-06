# Generated by Django 3.2.6 on 2021-08-31 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraphs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ThirdScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=250)),
                ('main_description', models.TextField()),
                ('sec_title', models.CharField(max_length=250)),
                ('sec_description', models.TextField()),
                ('thrd_title', models.CharField(max_length=250)),
                ('thrd_description', models.TextField()),
                ('image', models.ImageField(upload_to='states/third_screen/')),
                ('state', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='states.state')),
            ],
            options={
                'verbose_name_plural': 'Third Screen',
            },
        ),
        migrations.CreateModel(
            name='SecondScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=250)),
                ('main_description', models.TextField()),
                ('sec_title', models.CharField(max_length=250)),
                ('sec_description', models.TextField()),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.paragraphs')),
                ('state', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='states.state')),
            ],
            options={
                'verbose_name_plural': 'Second Screen',
            },
        ),
        migrations.CreateModel(
            name='FirstScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='states/first_screen/')),
                ('city', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='states.state')),
            ],
            options={
                'verbose_name_plural': 'First Screen',
            },
        ),
    ]
