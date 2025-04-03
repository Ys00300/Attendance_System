from django import forms
from AttendanceSystem.models import CustomUser

class StudentForms(forms.ModelForm):
    class Meta :
        model= CustomUser
        fields = ('__all__')