from django import forms
from AttendanceSystem.models import CustomUser
from .models import Student



class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['en_Number', 'profile_image','branch']
        widgets = {
            'en_Number': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make en_Number readonly
        }
        
class StudentForms(forms.ModelForm):
    class Meta :
        model= Student
        fields = []

