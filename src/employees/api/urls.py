from django.urls import path

from employees.api.views import EmployeesListView

app_name = 'employees_api'

urlpatterns = [
    path('employees/', EmployeesListView.as_view(), name='employees-list'),
]
