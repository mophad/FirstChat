from django import forms
from django.forms import ModelForm
from .models import User 

class SignupForm(ModelForm):

    class Meta:
        model = User
        fields = [
            "fullname",
            "username",
            "email",
            "password",
        ]

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password', 'name':'fullname'}),
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter a valid username!', 'name':'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'Please, enter your email!',  'name':'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder': 'Enter your password.', 'name':'password'})
        }


