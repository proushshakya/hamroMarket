from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login as auth_login, authenticate

# Create your views here.
from login.forms import LoginForm, SignupForm

from django.http import HttpResponse
import datetime

'''
#csrf = Cross site request forgery
@csrf_protect
def login(request):
	if request.method == 'POST':
		login = LoginForm(request.POST)
		if login.is_valid():
			return HttpResponse("Logged In")
		else:
			return HttpResponse("Error while logging in")
	else:
		csrfContext = RequestContext(request)
		login_form = LoginForm()
		return render(request,'login.html',{'form': login_form},csrfContext)
'''

@csrf_protect
def signup(request):
	if request.method == 'POST':
		signup = SignupForm(request.POST)
		if signup.is_valid():
			user = signup.save()
			user.set_password(user.password)
			user.save()
			username = user.username
			raw_password = signup.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			if user is not None:
				auth_login(request, user)
				return redirect('show/')

		return HttpResponse("Error while lregistering it")
	else:
		csrfContext = RequestContext(request)
		signup_form = SignupForm()
		return render(request,'register.html',{'form': signup_form},csrfContext)

def home(request):
	return render(request, 'home.html')

def setsession(request):
	request.session['name']='test'
	request.session['address']='ktm'
	return HttpResponse("session has been set.")

def getsession(request):
	name = request.session['name']
	address = request.session['address']
	return HttpResponse("Name: {0}, Address: {1}".format(name,address))

def setcookie(request):
	response = HttpResponse("Cookie has been set")
	response.set_cookie('age', datetime.datetime.now())
	return response

def getcookie(request):
	age = request.COOKIES['age']
	return HttpResponse("age: {0}".format(age))