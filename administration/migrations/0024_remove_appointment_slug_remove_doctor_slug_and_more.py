# Generated by Django 5.1.6 on 2025-02-11 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0023_remove_department_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='slug',
        ),
    ]
