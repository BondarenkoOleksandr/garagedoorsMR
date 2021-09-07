from rest_framework.generics import ListAPIView

from coupons.api.serializers import CouponSerializer
from coupons.models import Coupon


class CouponsListView(ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer