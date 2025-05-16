from django import forms
from django.contrib.auth.models import User
from .models import task, status
class TaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'perity', 'status', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
class RegisterForm(forms.ModelForm):
    # username = forms.CharField(label="username",max_length=100,required=True)
    # email = forms.EmailField(label="email",required=True)
    # password = forms.CharField(label="password",widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="confirm_password",widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))