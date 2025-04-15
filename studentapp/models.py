from django.db import models
from django.urls import reverse
from AttendanceSystem.models import CustomUser
# Create your models here.
from teacherapp.models import Teacher
   
class Student(models.Model):
    user = models.OneToOneField('AttendanceSystem.CustomUser',on_delete=models.CASCADE)
    teachers = models.ManyToManyField('teacherapp.Teacher', related_name='students', blank=True)
    
    def __str__(self):
        return f"{self.user.username} ({self.user.first_name})"