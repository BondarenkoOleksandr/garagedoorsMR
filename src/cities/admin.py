from django.contrib import admin

# Register your models here.
from cities.models import City, FirstScreen, SecondScreen, ThirdScreen, SEOCity


class FirstScreenInlines(admin.StackedInline):
    model = FirstScreen


class SecondScreenInlines(admin.StackedInline):
    model = SecondScreen


class ThirdScreenInlines(admin.StackedInline):
    model = ThirdScreen


class SEOCityInlines(admin.StackedInline):
    model = SEOCity


class RegionModelAdmin(admin.ModelAdmin):
    inlines = (FirstScreenInlines, SecondScreenInlines, ThirdScreenInlines, SEOCityInlines)
    search_fields = ['name']


admin.site.register(City, RegionModelAdmin)
