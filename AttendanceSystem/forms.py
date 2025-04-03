from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'forms-control'}),help_text='',)
    password1 = forms.CharField(max_length=10, label='Password', widget=forms.PasswordInput(attrs={'class':'forms-control'}),help_text='',)
    password2 = forms.CharField(max_length=10, label='Confirm password', widget=forms.PasswordInput(attrs={'class':'forms-control'}),help_text='',)
        
    
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','password1','password2','user_type']
        
    