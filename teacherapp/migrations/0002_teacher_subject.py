# Generated by Django 5.1.7 on 2025-04-13 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalAttendance', '0001_initial'),
        ('teacherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finalAttendance.subject'),
        ),
    ]
