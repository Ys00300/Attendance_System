# Generated by Django 5.1.7 on 2025-04-18 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalAttendance', '0002_alter_subject_course_code_alter_subject_subject_name'),
        ('studentapp', '0003_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentteacher',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.student'),
        ),
    ]
