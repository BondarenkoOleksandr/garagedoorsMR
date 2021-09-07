from django.urls import path

from coupons.api.views import CouponsListView

app_name = 'coupons_api'

urlpatterns = [
    path('coupons/', CouponsListView.as_view(), name='coupons-list'),
]
