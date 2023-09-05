from django.urls import path

from .views import index, edit_employee

app_name = 'employees'

urlpatterns = [
	path('employees/', index, name='index'),
	path('employees/<int:employee_id>/edit/', edit_employee, name='edit_employee')
]
