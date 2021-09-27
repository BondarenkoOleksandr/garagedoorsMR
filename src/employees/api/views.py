import json

from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from employees.api.serializers import EmployeeSerializer, ReviewSerializer
from employees.models import Employee, Review


class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request):
        employee_id = request.POST.get('employee', None)
        employee = Employee.objects.get(id=employee_id)
        name = request.POST.get('name', None)
        text = request.POST.get('text', None)
        rating = request.POST.get('rating', 5)
        review = model_to_dict(Review.objects.create(employee=employee, name=name, text=text, rating=rating))

        return JsonResponse(review, safe=False, json_dumps_params={'indent': 2})


class EmployeeDetailView(RetrieveAPIView):
    serializer_class = EmployeeSerializer

    def get(self, request, id):
        employee = Employee.objects.get(id=id)
        reviews = Review.objects.filter(employee=employee)
        reviews = [model_to_dict(review, fields=['name', 'text', 'rating']) for review in reviews]
        data = model_to_dict(employee, fields=['name', 'position', 'type_of_works'])
        data.update({'photo': request.build_absolute_uri(employee.photo.url)})
        data.update({'state': employee.state.name})
        data.update({'reviews': reviews})
        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


class EmployeeReviewList(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(employee__id=self.kwargs['id'])
