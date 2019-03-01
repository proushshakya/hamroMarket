from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ("username","password")
		labels = {
			'username': 'Username',
			'password': 'Password'
		}

		#selecting some fields
		#fields = ('first_name', 'last_name')

class SignupForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	confirmpassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ("username","first_name","last_name","email","password")
		labels = {
			'firstname': 'First name',
			'lastname': 'Last Name',
			'email': 'Email'
		}