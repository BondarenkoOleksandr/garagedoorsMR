from django.urls import path

from reviews.api.views import ReviewListView, ReviewDetailView

app_name = 'review_api'

urlpatterns = [
    path('reviews/', ReviewListView.as_view(), name='reviews-list'),
    path('reviews/<int:id>/', ReviewDetailView.as_view(), name='reviews-detail'),
]