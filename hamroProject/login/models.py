from django.db import models

# Create your models here.
class Login(models.Model):
	first_name = models.CharField(max_length=20)
	password = models.CharField(max_length=30)

class Register(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)
	confirmpassword = models.CharField(max_length=50)
