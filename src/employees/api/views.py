from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, get_object_or_404

from core.utils import queryset_pagination
from employees.api.serializers import EmployeeSerializer, EmployeeReviewSerializer
from employees.models import Employee, Review


class EmployeeListView(ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        employees = Employee.objects.all()
        return queryset_pagination(self.request, employees)


class EmployeeReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = EmployeeReviewSerializer

    def post(self, request):
        employee_id = request.POST.get('employee', None)
        employee = get_object_or_404(Employee, id=employee_id)
        name = request.POST.get('name', None)
        text = request.POST.get('text', None)
        rating = request.POST.get('rating', 5)
        review = model_to_dict(Review.objects.create(employee=employee, name=name, text=text, rating=rating))

        return JsonResponse(review, safe=False, json_dumps_params={'indent': 2})


class EmployeeDetailView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'slug'


class EmployeeReviewList(ListAPIView):
    serializer_class = EmployeeReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(employee__id=self.kwargs['id'])
