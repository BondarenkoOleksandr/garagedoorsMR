from django.forms import model_to_dict
from django.http import JsonResponse, Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404

from app.settings import base
from services.api.serializers import ServiceSerializer, ServiceCategorySerializer
from services.models import Service, ServiceCategory, ServiceArticle, ServiceReview


class ServicesListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServicesDetailView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, slug):
        service = Service.objects.filter(slug=slug)
        if not service:
            return JsonResponse(['Service not fount'], safe=False)
        article = ServiceArticle.objects.filter(article=service.first())
        reviews = ServiceReview.objects.filter(service=service.first())
        rev = []
        indx = 0
        for review in reviews:
            rev.append(model_to_dict(review, exclude=['logo', 'service', 'id']))
            rev[indx].update({'image': self.request.scheme + '://' + self.request.get_host() + review.logo.url,
                              'city': review.city.name,
                              'state': review.state.name})

            indx += 1

        image = service.first().image
        service = service.values('name', 'slug', 'category', 'excerpt').first()
        if image:
            service.update({'image': self.request.scheme + '://' + self.request.get_host() + image.image.url,
                            'alt': image.image.alt,
                            'title': image.image.title})

        if rev:
            service.update({'reviews': rev})

        if article:
            service.update({'article': model_to_dict(article.first())})

        return JsonResponse(service, safe=False, json_dumps_params={'indent': 2})


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
