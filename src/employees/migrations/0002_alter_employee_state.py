# Generated by Django 3.2.6 on 2021-08-28 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.state'),
        ),
    ]
