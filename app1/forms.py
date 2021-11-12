from django import forms
from django.forms import fields, widgets
from django.http.response import FileResponse
from .models import CustomUser, Books
from django.contrib.auth.forms import UserCreationForm

# Staff Signup Form
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email']
        labels = {'email':'Email'}
        widgets = {'first_name':forms.TextInput(attrs={'placeholder':'First name'}),
                    'last_name':forms.TextInput(attrs={'placeholder':'last name'}),
                    'email':forms.TextInput(attrs={'placeholder':'Email'}),
        }

# Book Form
class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author_name','published_date', 'available_status']