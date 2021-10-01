from django.contrib import admin

# Register your models here.
from cities.models import City, FirstScreen, SecondScreen, ThirdScreen


class FirstScreenInlines(admin.TabularInline):
    model = FirstScreen


class SecondScreenInlines(admin.TabularInline):
    model = SecondScreen


class ThirdScreenInlines(admin.TabularInline):
    model = ThirdScreen


class RegionModelAdmin(admin.ModelAdmin):
    inlines = (FirstScreenInlines, SecondScreenInlines, ThirdScreenInlines)
    search_fields = ['name']


admin.site.register(City, RegionModelAdmin)
