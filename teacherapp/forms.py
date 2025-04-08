from django import forms
from AttendanceSystem.models import CustomUser

class TeacherForms(forms.ModelForm):
    class Meta :
        model= CustomUser
        fields = ('gender','branch','en_Number')
