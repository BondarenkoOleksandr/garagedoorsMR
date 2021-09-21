import json

from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView

from reviews.api.serializers import ReviewSerializer
from reviews.models import Review


class ReviewListView(ListAPIView):

    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all()
        data = {}
        for review in reviews:
            model = model_to_dict(review, exclude=['id', 'logo', 'city', 'state'])
            model.update({'logo': request.build_absolute_uri(review.logo.url)})
            model.update({'city': review.city.name})
            model.update({'state': review.state.name})
            data.update({review.id: model})

        return JsonResponse(data)


class ReviewDetailView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, id):
        review = Review.objects.get(id=id)
        data = []
        model = model_to_dict(review, exclude=['logo', 'city', 'state'])
        model.update({'logo': request.build_absolute_uri(review.logo.url)})
        model.update({'city': review.city.name})
        model.update({'state': review.state.name})
        data.append(model)

        return JsonResponse(*data)