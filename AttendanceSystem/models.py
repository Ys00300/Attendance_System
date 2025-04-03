from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

class CustomUser(AbstractUser):
    gender = models.CharField(max_length=10, choices=[('M', 'Male'),('F','Female')], null=True, blank=True)
    section = models.CharField(max_length=10, choices=[('A', 'Section A'), ('B', 'Section B'), ('C', 'Section C'), ('D', 'Section D')], null=True, blank=True)
    branch = models.CharField(max_length=100 )
    en_Number = models.CharField(max_length=100,unique=True, null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')

    # phone_number = models.CharField(max_length=15, null=True, blank=True)
    # profile_image = models.ImageField(upload_to='image/',null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

    def get_absolute_url(self):
        return reverse("detail_student", kwargs={"pk": self.pk})

