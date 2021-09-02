from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.core import serializers

from cities.api.serializers import CitySerializer
from cities.models import City
from core.utils import add_images_path
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
        data = {}
        for state in states:
            data.update({state.name: [city for city in City.objects.filter(state=state).values('name')]})

        return JsonResponse(data)


class CityDetailView(RetrieveAPIView):

    def get(self, request, id):
        city = City.objects.get(id=id)
        data = model_to_dict(city, fields=['name'])
        data.update({'state': city.state.name, 'first_screen': model_to_dict(city.firstscreen, exclude=['image']),
                     'second_screen': model_to_dict(city.secondscreen),
                     'third_screen': model_to_dict(city.thirdscreen, exclude=['image'])})

        data = add_images_path(request, city, data)
        return JsonResponse(data)
