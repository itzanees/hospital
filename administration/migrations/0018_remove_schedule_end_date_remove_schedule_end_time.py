# Generated by Django 5.1.4 on 2025-02-10 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0017_remove_department_profile_updated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='end_time',
        ),
    ]
