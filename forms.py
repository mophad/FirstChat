from django import forms
from django.forms import ModelForm
from .models import User , Page_Setting , Create_Acct, Create_Company , Open_Ai, Bot_Acct

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
            "address",
            "email",
            "favicon",
            "admin_page_logo",
            "login_page_logo",
            "admin_login_image",
            "chat_color",
            "footer_text"
            
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Tittle for your page','name':'fullname'}),
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter a valid address!', 'name':'username'}),
            'email': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Please, enter your email!',  'name':'email'}),
            'favicon': forms.FileInput(attrs={'class': 'form-control' ,'name':'password'}),
            'admin_page_logo': forms.FileInput(attrs={'class': 'form-control' ,'name':'password'}),
            'login_page_logo': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
            'admin_login_image': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
            'chat_color': forms.TextInput(attrs={'class': 'form-control' , 'type': 'color','name':'password'}),
            'footer_text': forms.Textarea(attrs={'class': 'form-control',  'placeholder': 'Enter Footter text.', 'name':'password'}),
            
        }


class Create_User(ModelForm):

    class Meta:
        model = Create_Acct

        fields = [
            "Fname",
            "Lname",
            "address",
            "email",
            "password",
            "username",
            "picture",
            "user_type",            
        ]

        widgets = {
            'Fname': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Your valid name','name':'Fname'}),
            'Lname': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Please enter a valid name!','name':'Lname'}),
            'address': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Please, enter correct address!','name':'address'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' ,'placeholder':' Enter valid Email', 'name': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control' ,'placeholder':'Enter password', 'name': 'password'}),
            'username': forms.TextInput(attrs={'class': 'form-control' ,  'placeholder':'Enter username', 'name': 'username'}),
            'picture': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
            'user_type': forms.TextInput(attrs={'class': 'form-control' , 'name':'user_type', 'type':'hidden'}),
            
        }


class Create_Company_Acct(ModelForm):

    class Meta:
        model = Create_Company

        fields = [
            "name",
            "address",
            "email",
            "username",
            "picture",
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Your valid name', 'name':'fullname'}),
            'address': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Please, enter correct address!','name':'email'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' ,'placeholder':' Enter valid Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control' ,  'placeholder':'Enter username'}),
            'picture': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
            
        }


class Open_Ai_Acct(ModelForm):

    class Meta:
        model = Open_Ai

        fields = [
            "api_key",
            "model",
            "system_role",
            "prompt",
            "picture",
        ]

        widgets = {
            'api_key': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Your valid name','name':'fullname'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a ChatGpt model!','name':'username'}),
            'system_role': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'E.g i want you to act as doctor','name':'email'}),
            'prompt': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'E.g  i want you only react to patient that have blood pressure'}),
            'picture': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
            
        }




class Bot_Set(ModelForm):

    class Meta:
        model = Bot_Acct

        fields = [
            "name",
            "dialogflow",
            "picture",
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your valid name','name':'fullname'}),
            'dialogflow': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a valid URL!','name':'username'}),
            'picture': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
            
        }
