# forms.py
from django import forms
from datetime import date

class EmailForm(forms.Form):
    from_date = forms.DateField(
        initial=date.today, 
        widget=forms.SelectDateWidget(years=range(2000, 2101))
    )
    to_date = forms.DateField(
        initial=date.today, 
        widget=forms.SelectDateWidget(years=range(2000, 2101))
    )
    cc_teacher = forms.EmailField(required=False, label="CC Teacher (Optional)")
    reason = forms.CharField(widget=forms.Textarea, label="Reason", required=True)
