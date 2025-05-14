from django import forms
from .models import task, status
class TaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'perity', 'status', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }