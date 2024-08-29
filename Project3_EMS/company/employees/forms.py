from django import forms
from .models import Department, Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'department']

class EmployeeDepartment(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'location']       
