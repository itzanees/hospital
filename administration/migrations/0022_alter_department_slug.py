# Generated by Django 5.1.6 on 2025-02-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0021_doctor_profile_updated_staff_profile_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.SlugField(max_length=32),
        ),
    ]
