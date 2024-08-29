from django.shortcuts import get_object_or_404, render, redirect
from employees.models import Department, Employee
from .forms import EmployeeDepartment, EmployeeForm
# Create your views here.

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form})

# def employee_list(request):
#     employees = Employee.objects.select_related('department').all()
#     return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_list(request):
    department_id = request.GET.get('department')
    if department_id:
        employees = Employee.objects.filter(department_id=department_id)
    else:
        employees = Employee.objects.select_related('department').all()
    departments = Department.objects.all()
    return render(request, 'employees/employee_list.html', {
        'employees': employees,
        'departments': departments,
    })

def add_department(request):
    if request.method == 'POST':
        form = EmployeeDepartment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeDepartment()
    return render(request, 'employees/add_department.html', {'form': form})
