from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView

from core.utils import add_images_path
from states.api.serializers import StateSerializer
from states.models import State


class StateListView(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateDetailView(ListAPIView):

    def get(self, request, slug):
        state = State.objects.get(slug=slug)
        data = model_to_dict(state, fields=['name', 'slug'])
        data.update({'first_screen': model_to_dict(state.firstscreen, exclude=['image', 'state']),
                     'second_screen': model_to_dict(state.secondscreen, exclude=['state']),
                     'third_screen': model_to_dict(state.thirdscreen, exclude=['image', 'state']),
                     'seo': model_to_dict(state.seo)})
        data = add_images_path(request, state, data)
        return JsonResponse(data)
