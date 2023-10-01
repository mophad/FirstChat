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

class App_Customize(ModelForm):

    class Meta:
        model = Page_Setting
        fields = [
            "title",
            "footertext",
            "address",
            "email",
            "number",
            "favicon",
            "pagelogo",
            "signuplogo",
            
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter your password',
                                               'name':'fullname'}),
            'footertext': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Please enter a valid username!',
                                                   'name':'username'}),
            'address': forms.TextInput(attrs={'class': 'form-control' ,
                                                'placeholder': 'Please, enter your email!', 
                                                  'name':'email'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' , 
                                                'placeholder': 'Enter your password.',
                                                  'name':'password'}),
            'number': forms.NumberInput(attrs={'class': 'form-control' ,
                                                  'placeholder': 'Enter your password.',
                                                    'name':'password'}),
            'favicon': forms.FileInput(attrs={'class': 'form-control' , 
                                                  'placeholder': 'Enter your password.',
                                                    'name':'password'}),
            'pagelogo': forms.FileInput(attrs={'class': 'form-control' , 
                                                   'placeholder': 'Enter your password.', 
                                                   'name':'password'}),
            'signuplogo': forms.FileInput(attrs={'class': 'form-control' ,
                                                      'placeholder': 'Enter your password.',
                                                        'name':'password'}),



        }


