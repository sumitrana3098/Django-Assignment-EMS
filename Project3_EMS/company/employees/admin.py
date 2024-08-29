from django.contrib import admin

from employees.models import Department, Employee

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)