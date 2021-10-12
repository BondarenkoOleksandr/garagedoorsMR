from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView


def index(request):
    return render(request=request, template_name='index.html')


def login(request):
    return render(request=request, template_name='login.html')


class SitemapView(APIView):

    def get(self, request, *args, **kwargs):
        return JsonResponse('waiting for array...', safe=False)
