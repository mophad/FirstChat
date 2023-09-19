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
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password',}),
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter a valid Email adddress!',}),
            'email': forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'Please, enter your name!',}),
            'password': forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder': 'Please choose a username.',})
        }


