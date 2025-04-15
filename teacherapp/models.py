from django.db import models

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField('AttendanceSystem.CustomUser',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/',null=True)
    
    
    def __str__(self):
        return f"{self.user.username} ({self.user.first_name})"