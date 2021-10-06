from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView

from services.api.serializers import ServiceSerializer, ServiceCategorySerializer
from services.models import Service, ServiceCategory


class ServicesListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServicesDetailView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug'


class ServiceCategoryView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self, slug):
        return Service.objects.filter(category__slug=slug)

class ServiceCategoryListView(ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer