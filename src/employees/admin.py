from django.contrib import admin

# Register your models here.
from employees.models import Employee, Review


class EmployeeInlines(admin.TabularInline):
    model = Review


class EmployeeAdmin(admin.ModelAdmin):
    inlines = (EmployeeInlines,)
    search_fields = ['name']


admin.site.register(Employee, EmployeeAdmin)
