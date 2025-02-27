# Generated by Django 5.1.4 on 2025-02-13 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0025_alter_medicalrecord_diagnosis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='diagnosis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='prescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='treatment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
