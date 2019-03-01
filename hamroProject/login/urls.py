from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
	path('home', views.home, name='home'),
	#path(''. views.login),
	path('register/', views.signup, name='register')
]