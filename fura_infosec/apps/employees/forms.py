from django import forms

from .models import Employee


class QuickEmployeeForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = ['lastname', 'firstname', 'middlename', 'email']
		labels = {
			'lastname': 'Фамилия',
			'firstname': 'Имя',
			'middlename': 'Отчество',
			'email': 'Адрес корпоративной почты',
		}


class EmployeeForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = "__all__"
		# exclude = ('status',)
		labels = {
			'lastname': 'Фамилия',
			'firstname': 'Имя',
			'middlename': 'Отчество',
			'email': 'Адрес корпоративной почты',
			'phone': 'Номер корпоративного телефона',
			'department': 'Департамент',
			'position': 'Должность',
			'device': 'Устройство',
			'user_lic': 'Лицензия пользователя',
			'status': 'Статус отслеживания',
			'dossier': 'Досье сотрудника'
		}
