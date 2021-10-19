from django.forms import model_to_dict
from django.http import JsonResponse, Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404

from app.settings import base
from services.api.serializers import ServiceSerializer, ServiceCategorySerializer, ServiceDetailSerializer
from services.models import Service, ServiceCategory, ServiceArticle, ServiceReview


class ServicesListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServicesDetailView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer
    lookup_field = 'slug'


class ServiceCategoryView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, slug):
        services = Service.objects.filter(category__slug=slug).values('id', 'name', 'slug', 'excerpt')
        print(services)

        return JsonResponse(list(services), safe=False, json_dumps_params={'indent': 2})


class ServiceCategoryListView(ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
