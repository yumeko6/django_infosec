from django.contrib import admin

from .models import Employee, Department, Position, Device


class EmployeeAdmin(admin.ModelAdmin):
	fields = [
		'lastname',
		'firstname', 'middlename', 'email',
		'phone', 'user_lic', 'status', 'dossier',
		'department', 'position', 'device'
	]
	list_display = [
		'id', 'lastname',
		'firstname', 'middlename', 'email',
		'phone', 'user_lic', 'status', 'dossier',
		'department', 'position', 'device'
	]
	search_fields = [
		'lastname', 'firstname',
		'email', 'phone'
	]


class DepartmentAdmin(admin.ModelAdmin):
	fields = ['dept_name']
	list_display = ['id', 'dept_name']
	search_fields = ['dept_name']


class PositionAdmin(admin.ModelAdmin):
	fields = ['pos_name']
	list_display = ['pos_name']
	search_fields = ['pos_name']


class DeviceAdmin(admin.ModelAdmin):
	fields = ['dev_name', 'device_lic']
	list_display = ['dev_name', 'device_lic']
	search_fields = ['dev_name']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Device, DeviceAdmin)
