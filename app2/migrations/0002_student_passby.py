# Generated by Django 5.0.2 on 2024-03-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passby',
            field=models.CharField(default=None, max_length=50),
        ),
    ]