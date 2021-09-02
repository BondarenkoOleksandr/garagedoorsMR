from django.urls import path

from cities.api.views import CitiesListView

app_name = 'cities_api'

urlpatterns = [
    path('cities/', CitiesListView.as_view(), name='cities-list'),
]
