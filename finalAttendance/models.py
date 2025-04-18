from django.db import models
from AttendanceSystem.models import CustomUser
from teacherapp.models import Teacher
from studentapp.models import Student
# Create your models here.

class Subject(models.Model):
    SUBJECT_CHOICES = [
        ('ML', 'Machine Learning'),
        ('AI', 'Artificial Intelligence'),
        ('DS', 'Data Science'),
    ]

    SUBJECT_CODES = {
        'ML': 'ML0030',
        'AI': 'AI0020',
        'DS': 'DS0040',
    }
 
    subject_name = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    course_code = models.TextField(max_length=10, unique=True, blank=True)
    teachers = models.ForeignKey('teacherapp.Teacher', related_name='subjects', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Automatically assign course_code based on subject_name
        if self.subject_name in self.SUBJECT_CODES:
            self.course_code = self.SUBJECT_CODES[self.subject_name]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject_name} ({self.course_code})"
    
class StudentTeacher(models.Model):
    student = models.ForeignKey('AttendanceSystem.CustomUser',on_delete=models.CASCADE,related_name='student_teacher')
    teacher = models.ForeignKey('teacherapp.Teacher',on_delete=models.CASCADE,related_name='teacher_student')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='student_teacher_links')
    # student = models.ForeignKey('studentapp.Student', on_delete=models.CASCADE)

class Attendance(models.Model):
    student_teacher = models.ForeignKey('StudentTeacher', on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField(auto_now_add=True)  # You can also manually specify the date
    status = models.CharField(
        max_length=10, 
        choices=[('Present', 'Present'),('Leave', 'Leave')]
    )

    def __str__(self):        
        return f"{self.student_teacher.student.username} - {self.date} - {self.status}"
