from django.contrib import admin

# Register your models here.
from employees.models import Employee, State, Review


class EmployeeInlines(admin.TabularInline):
    model = Review


class EmployeeAdmin(admin.ModelAdmin):
    inlines = (EmployeeInlines,)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(State)
# admin.site.register(Review)
