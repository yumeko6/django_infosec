from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import QuickEmployeeForm, EmployeeForm
from .models import Employee


@login_required
def index(request):
	employees = Employee.objects.all()
	quick_create_form = QuickEmployeeForm(request.POST or None)
	if quick_create_form.is_valid():
		employee = quick_create_form.save(commit=False)
		employee.save()
		return redirect('employees:index')
	context = {
		'employees': employees,
		'title': 'FURA IS: Employees',
		'form': quick_create_form
	}
	return render(request, 'employees/nwe_old_index.html', context)


@login_required
def edit_employee(request, employee_id):
	is_edit = True
	employee = get_object_or_404(Employee, pk=employee_id)
	employees = Employee.objects.all()
	form = EmployeeForm(request.POST or None, instance=employee)
	if form.is_valid():
		form.save()
		return redirect('employees:index')
	context = {
		'employee': employee,
		'employees': employees,
		'form': form,
		'is_edit': is_edit,
		'employee_id': employee_id,
		'title': 'FURA IS: Edit employee',
	}
	return render(request, 'employees/nwe_old_index.html', context)
