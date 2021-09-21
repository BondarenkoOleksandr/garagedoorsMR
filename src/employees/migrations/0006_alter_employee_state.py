# Generated by Django 3.2.6 on 2021-08-31 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0001_initial'),
        ('employees', '0005_auto_20210831_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='states.state'),
        ),
    ]