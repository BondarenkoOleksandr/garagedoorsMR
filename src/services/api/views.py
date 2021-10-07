from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404

from app.settings import base
from services.api.serializers import ServiceSerializer, ServiceCategorySerializer
from services.models import Service, ServiceCategory, ServiceArticle


class ServicesListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServicesDetailView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, slug):
        service = Service.objects.filter(slug=slug)
        article = get_object_or_404(ServiceArticle, article=service.first())
        image_link = self.request.scheme + '://' + self.request.get_host()+ '/' + base.MEDIA_URL + service.image,
        service = model_to_dict(service.first(), exclude=['image'])
        service.update({'image': image_link,
                        'article': model_to_dict(article)})

        return JsonResponse(list(service), safe=False, json_dumps_params={'indent': 2})


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
