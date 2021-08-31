from django.contrib import admin

# Register your models here.
from states.models import State, FirstScreen, SecondScreen, ThirdScreen


class FirstScreenInlines(admin.TabularInline):
    model = FirstScreen


class SecondScreenInlines(admin.TabularInline):
    model = SecondScreen


class ThirdScreenInlines(admin.TabularInline):
    model = ThirdScreen


class StatesModelAdmin(admin.ModelAdmin):
    inlines = (FirstScreenInlines, SecondScreenInlines, ThirdScreenInlines,)


admin.site.register(State, StatesModelAdmin)
