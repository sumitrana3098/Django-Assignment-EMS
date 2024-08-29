from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:pk>/', views.update_employee, name='update_employee'),
    path('department/', views.add_department, name='add_department'),
]
