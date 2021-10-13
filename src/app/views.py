from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

import xml.etree.cElementTree as ET


def index(request):
    return render(request=request, template_name='index.html')


def login(request):
    return render(request=request, template_name='login.html')


class SitemapView(APIView):

    def get(self, request, *args, **kwargs):

        urlset = ET.Element("urlset")
        for i in range(10):
            doc = ET.SubElement(urlset, "url")
            ET.SubElement(doc, "loc").text = "link"
            ET.SubElement(doc, "lastmod").text = "link"

        tree = ET.ElementTree(urlset)
        tree.write("filename.xml")

        return JsonResponse('waiting for array...', safe=False)
