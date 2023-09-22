# import the standard Django Model
# from built-in library
from django.db import models
from django.contrib.auth.models import AbstractUser



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
	

# class Login_E(AbstractUser):
#     email = models.EmailField(unique=True)
