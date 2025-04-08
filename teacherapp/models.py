from django.db import models

# Create your models here.
class Teacher(models.Model):
    
    subject = models.CharField(max_length=50)
    user = models.OneToOneField('AttendanceSystem.CustomUser',on_delete=models.CASCADE, null= True)
    image = models.ImageField(upload_to='images/',null=True)
    
    def __str__(self):
        return self.subject