from django import forms
from AttendanceSystem.models import CustomUser
from .models import Teacher
from finalAttendance.models import Subject


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['en_Number', 'profile_image','branch']
        widgets = {
            'en_Number': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make en_Number readonly
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [] 
        
        
# class TeacherForm(forms.ModelForm):
#     class Meta :
#         model= Teacher     
#         fields = ['subject','en_Number','profile_image']
#         exclude = ['password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'date_joined']
        

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name']
        widgets = {
            'subject_name': forms.Select(attrs={'class': 'form-control', 'id': 'id_subject_name'}),
            'course_code': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control', 'id': 'id_course_code'}),
        }
        labels = {
            'subject_name': 'Select Subject',
            'course_code': 'Course Code',
        }