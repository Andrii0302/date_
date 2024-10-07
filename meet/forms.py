from django import forms
from .models import DateTable

class DateForm(forms.ModelForm):
    class Meta:
        model = DateTable
        fields = ['date','time','name']
        labels = {
            'date': 'Pick a date (2024-12-01)',
            'time': 'Pick a time (00:00:00)',
            'name':'Add a comment if you want to'
        }
