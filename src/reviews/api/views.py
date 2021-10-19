from rest_framework.generics import ListAPIView, RetrieveAPIView

from reviews.api.serializers import ReviewSerializer
from reviews.models import Review


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
