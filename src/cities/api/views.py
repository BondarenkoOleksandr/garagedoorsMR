from rest_framework.generics import ListAPIView

from cities.api.serializers import CitySerializer
from cities.models import City


class CitiesListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        cities = City.objects.order_by('state')
        return cities