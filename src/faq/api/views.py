from rest_framework.generics import ListAPIView

from faq.api.serializers import FAQSerializer
from faq.models import FAQ


class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class FAQByServiceView(ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        return FAQ.objects.filter(service__id=self.kwargs['id'])
