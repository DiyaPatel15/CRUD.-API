# Generated by Django 5.0.1 on 2024-03-08 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_student_passby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='city',
        ),
        migrations.RemoveField(
            model_name='student',
            name='passby',
        ),
    ]
