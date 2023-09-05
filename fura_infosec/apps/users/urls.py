from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path


app_name = 'users'

urlpatterns = [
	path(
		'logout/',
		LogoutView.as_view(template_name='users/login.html'),
		name='logout'
	),
	path(
		'login/',
		LoginView.as_view(template_name='users/login.html'),
		name='login'
	),
]
