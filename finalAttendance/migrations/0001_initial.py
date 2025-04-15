# Generated by Django 5.1.7 on 2025-04-13 10:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacherapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_teacher', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_student', to='teacherapp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Leave', 'Leave')], max_length=10)),
                ('student_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to='finalAttendance.studentteacher')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.TextField(max_length=10, unique=True)),
                ('subject_name', models.CharField(max_length=20)),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='teacherapp.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='studentteacher',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_teacher_links', to='finalAttendance.subject'),
        ),
    ]
