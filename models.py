# import the standard Django Model
# from built-in library
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator






class UserModel(models.Model):

	# fields of the model
	fullname = models.CharField(max_length = 200)
	username = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)
	password = models.CharField( max_length=100, default=20)
	# renames the instances of the model
	# with their title name
	def __str__(self):
		return self.fullname

class User(models.Model):

	# fields of the model
	fullname = models.CharField(max_length = 200)
	username = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)
	password = models.CharField( max_length=100, default=20)
	# renames the instances of the model
	# with their title name
	def __str__(self):
		return self.fullname

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Article(models.Model):

	# fields of the model
	title = models.CharField(max_length = 200)
	boytext = models.CharField(max_length=200)
	def __str__(self):
		return self.title	

# class Login_E(AbstractUser):
#     email = models.EmailField(unique=True)

class Color(models.CharField):
    default_validators = [RegexValidator(
        regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
        message='Enter a valid color code in hexadecimal format (e.g., #RRGGBB or #RGB).',
        code='invalid_color'
    )]
    
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7
        kwargs['validators'] = self.default_validators
        super().__init__(*args, **kwargs)




class Page_Setting(models.Model):

	title = models.CharField(max_length = 200)
	address = models.CharField(max_length = 200)
	email = models.EmailField(max_length=200)
	favicon = models.ImageField (upload_to ='assets/img/', default='assets/img/logo.png')
	admin_page_logo = models.ImageField( upload_to='assets/img/',default='assets/img/logo.png' )
	login_page_logo = models.ImageField( upload_to='assets/img/', default='assets/img/logo.png' )
	admin_login_image = models.ImageField( upload_to='assets/img/', default='assets/img/logo.png' )
	chat_color = Color(default=2)
	footer_text = models.CharField(max_length = 200)



	# renames the instances of the model
	# with their title name
	def __str__(self):
		return self.title
	

class Create_Acct(models.Model):
	Fname = models.CharField(max_length = 200 ,default='hmmmed')
	Lname = models.CharField(max_length = 200 , default='adepoju')
	address = models.EmailField(max_length=200 , default='ayekale')
	email = models.EmailField (max_length=200 , default='hammed@gmail.com')
	password = models.CharField(max_length=200,default='hammed' )
	username = models.CharField(max_length=200 , default='adppoju')
	picture = models.ImageField( upload_to='assets/img/', default='assets/img/logo.png' )
	user_type = models.CharField(max_length = 200 , default='visitor')


	def __str__(self):
		return self.Fname
	


class Create_Company(models.Model):
	name = models.CharField(max_length = 200 ,default='hmmmed')
	address = models.CharField(max_length=200 , default='ayekale')
	email = models.EmailField (max_length=200 , default='hammed@gmail.com')
	username = models.CharField(max_length=200 , default='adppoju')
	picture = models.ImageField( upload_to='assets/img/', default='assets/img/logo.png' )


	def __str__(self):
		return self.name
	


class Open_Ai(models.Model):
	api_key = models.CharField(max_length = 200 ,default='hmmmed')
	model = models.CharField(max_length = 200 , default='adepoju')
	system_role = models.CharField(max_length=200 , default='ayekale')
	prompt = models.CharField (max_length=200 , default='hammedgmailcom')
	picture = models.ImageField( upload_to='assets/img/', default='assets/img/logo.png' )

	def __str__(self):
		return self.system_role
	

class Bot_Acct(models.Model):
	dialogflow = models.URLField(max_length = 200, null=True)
	name = models.CharField(max_length = 200 , default='adepoju')
	picture = models.ImageField( upload_to='assets/img/', default='assets/img/logo.png' )

	def __str__(self):
		return self.name
	
