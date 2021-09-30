from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.core import serializers

from cities.api.serializers import CitySerializer
from cities.models import City
from core.utils import add_images_path, queryset_pagination
from states.models import State


class CitiesListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        cities = City.objects.order_by('state')
        return cities


class CitiesByStates(ListAPIView):
    serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        states = State.objects.all()
        states = queryset_pagination(request, states)
        data = []
        for state in states:
            data.append({state.name: [city for city in queryset_pagination(City.objects.filter(state=state).values('id', 'name', 'slug'))]})

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


class CityDetailView(RetrieveAPIView):

    def get(self, request, slug):
        city = City.objects.get(slug=slug)
        data = model_to_dict(city, fields=['name', 'description'])
        data.update({'state': city.state.name, 'first_screen': model_to_dict(city.firstscreen, exclude=['image']),
                     'second_screen': model_to_dict(city.secondscreen),
                     'third_screen': model_to_dict(city.thirdscreen, exclude=['image'])})

        data = add_images_path(request, city, data)
        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})
