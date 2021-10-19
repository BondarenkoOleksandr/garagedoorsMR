from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView

from core.utils import add_images_path
from states.api.serializers import StateSerializer, StateDetailSerializer
from states.models import State


class StateListView(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateDetailView(RetrieveAPIView):
    queryset = State.objects.all()
    serializer_class = StateDetailSerializer
    lookup_field = 'slug'
