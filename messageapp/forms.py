from django import forms
from .models import Message

class EmailForm(forms.Form):
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    recipient = forms.EmailField()