from django import forms
from datetime import date

class EmailForm(forms.Form):
    from_date = forms.DateField(initial=date.today, widget=forms.SelectDateWidget(years=range(2000, 2101)))
    to_date = forms.DateField(initial=date.today, widget=forms.SelectDateWidget(years=range(2000, 2101)))
    cc_teacher = forms.EmailField(required=False, label="CC Teacher (Optional)")
    reason = forms.CharField(widget=forms.Textarea, label="Reason", required=True)
    
    # Adding a choice to select whether to send email to student or teacher
    RECIPIENT_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    
    recipient_type = forms.ChoiceField(choices=RECIPIENT_CHOICES, label="Send Email To", required=True)

