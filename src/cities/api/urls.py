from django.urls import path

from cities.api.views import CitiesListView, CitiesByStates, CityDetailView

app_name = 'cities_api'

urlpatterns = [
    path('cities/', CitiesByStates.as_view(), name='cities-list'),
    path('cities/<int:id>/', CityDetailView.as_view(), name='city-detail')
]
