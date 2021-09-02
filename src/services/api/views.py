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
    def get(self, request, slug):
        services = Service.objects.filter(category__slug=slug)
        data = {}
        cat = ServiceCategory.objects.get(slug=slug)
        data.update({cat.name: model_to_dict(service, exclude=['image']) for service in services})

        return JsonResponse(data)


class ServiceCategoryListView(ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer