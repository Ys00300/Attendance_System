from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.


# yourapp/models.py

import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

def generate_en_number(user_type="student"):
    from .models import CustomUser  # Needed only for uniqueness check
    while True:
        random_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        prefix = "T_id" if user_type == "teacher" else "EN"
        full_id = f"{prefix}{random_number}"
        if not CustomUser.objects.filter(en_Number=full_id).exists():
            return full_id

class CustomUser(AbstractUser):
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F','Female')], null=True, blank=True)
    section = models.CharField(max_length=10, choices=[('A', 'Section A'), ('B', 'Section B'), ('C', 'Section C'), ('D', 'Section D')], null=True, blank=True)
    branch = models.CharField(max_length=100)
    en_Number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    profile_image = models.ImageField(upload_to='image/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.en_Number:
            self.en_Number = generate_en_number(self.user_type)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

    def get_absolute_url(self):
        return reverse("detail_student", kwargs={"pk": self.pk})

















# class CustomUser(AbstractUser):
#     gender = models.CharField(max_length=10, choices=[('M', 'Male'),('F','Female')], null=True, blank=True)
#     section = models.CharField(max_length=10, choices=[('A', 'Section A'), ('B', 'Section B'), ('C', 'Section C'), ('D', 'Section D')], null=True, blank=True)
#     branch = models.CharField(max_length=100 )
#     en_Number = models.CharField(max_length=100,unique=True, null=True, blank=True)
#     date_of_creation = models.DateTimeField(auto_now_add=True)
    
#     USER_TYPE_CHOICES = [
#         ('student', 'Student'),
#         ('teacher', 'Teacher'),
#     ]
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
#     # subject = models.CharField(max_length=10,null=True,blank=True)
    
#     profile_image = models.ImageField(upload_to='image/',null=True,blank=True)

#     def __str__(self):
#         return f"{self.username} ({self.get_user_type_display()})"

#     def get_absolute_url(self):
#         return reverse("detail_student", kwargs={"pk": self.pk})

