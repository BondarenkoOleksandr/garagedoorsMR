from django.contrib import admin

# Register your models here.
from states.models import State, FirstScreen, SecondScreen, ThirdScreen, SEOState


class FirstScreenInlines(admin.StackedInline):
    model = FirstScreen


class SecondScreenInlines(admin.StackedInline):
    model = SecondScreen


class ThirdScreenInlines(admin.StackedInline):
    model = ThirdScreen


class SEOStateInlines(admin.StackedInline):
    model = SEOState


class StatesModelAdmin(admin.ModelAdmin):
    inlines = (FirstScreenInlines, SecondScreenInlines, ThirdScreenInlines,)


admin.site.register(State, StatesModelAdmin)
