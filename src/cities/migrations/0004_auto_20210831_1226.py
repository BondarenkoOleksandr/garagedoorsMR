# Generated by Django 3.2.6 on 2021-08-31 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_auto_20210831_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='first_screen',
        ),
        migrations.RemoveField(
            model_name='city',
            name='second_screen',
        ),
        migrations.RemoveField(
            model_name='city',
            name='third_screen',
        ),
        migrations.RemoveField(
            model_name='state',
            name='first_screen',
        ),
        migrations.RemoveField(
            model_name='state',
            name='second_screen',
        ),
        migrations.RemoveField(
            model_name='state',
            name='third_screen',
        ),
        migrations.AddField(
            model_name='firstscreen',
            name='city',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.city'),
        ),
        migrations.AddField(
            model_name='firstscreen',
            name='state',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.state'),
        ),
        migrations.AddField(
            model_name='secondscreen',
            name='city',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.city'),
        ),
        migrations.AddField(
            model_name='secondscreen',
            name='state',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.state'),
        ),
        migrations.AddField(
            model_name='thirdscreen',
            name='city',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.city'),
        ),
        migrations.AddField(
            model_name='thirdscreen',
            name='state',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.state'),
        ),
    ]
