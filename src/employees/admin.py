from django.contrib import admin

# Register your models here.
from employees.models import Employee, State

admin.site.register(Employee)
admin.site.register(State)