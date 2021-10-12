from django.contrib import admin

# Register your models here.
from employees.models import Employee, Review, SEOEmployee


class EmployeeInlines(admin.StackedInline):
    model = Review


class SEOEmployeeInlines(admin.StackedInline):
    model = SEOEmployee


class EmployeeAdmin(admin.ModelAdmin):
    inlines = (EmployeeInlines, SEOEmployeeInlines)
    search_fields = ['name']


admin.site.register(Employee, EmployeeAdmin)
