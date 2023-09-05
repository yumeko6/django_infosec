from django.db import models


YES = 'YES'
NO = 'NO'
SIMPLE_CHOICES = [
	(YES, 'Да'),
	(NO, 'Нет')
]


class Department(models.Model):
	dept_name = models.CharField(max_length=100, verbose_name='Департамент')

	def __str__(self):
		return self.dept_name


class Position(models.Model):
	pos_name = models.CharField(max_length=100, verbose_name='Должность')

	def __str__(self):
		return self.pos_name


class Device(models.Model):
	dev_name = models.CharField(max_length=10, verbose_name='Устройство')
	device_lic = models.CharField(
		max_length=3, choices=SIMPLE_CHOICES,
		default=NO, verbose_name='Лицензия устройства',
	)

	def __str__(self):
		return self.dev_name


class Employee(models.Model):
	firstname = models.CharField(max_length=15, verbose_name='Имя')
	lastname = models.CharField(max_length=30, verbose_name='Фамилия')
	middlename = models.CharField(max_length=30, verbose_name='Отчество')
	email = models.EmailField(unique=True, blank=False, verbose_name='Почта')
	phone = models.PositiveIntegerField(
		unique=True, blank=True, verbose_name='Телефон', null=True
	)
	user_lic = models.CharField(
		max_length=3, choices=SIMPLE_CHOICES,
		default=NO, verbose_name='Лицензия пользователя', blank=True
	)
	status = models.CharField(
		max_length=3, choices=SIMPLE_CHOICES,
		default=NO,	verbose_name='Статус отслеживания', blank=True)
	dossier = models.CharField(
		max_length=3, choices=SIMPLE_CHOICES,
		default=NO, verbose_name='Досье сотрудника', blank=True
	)

	department = models.ForeignKey(
		Department, on_delete=models.DO_NOTHING, related_name='department', blank=True, null=True
	)
	position = models.ForeignKey(
		Position, on_delete=models.DO_NOTHING, related_name='position', blank=True, null=True
	)
	device = models.OneToOneField(
		Device, on_delete=models.DO_NOTHING, related_name='device', blank=True, null=True
	)

	def __str__(self):
		return f'{self.lastname} {self.firstname}'
