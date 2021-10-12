from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, get_object_or_404

from core.utils import queryset_pagination
from employees.api.serializers import EmployeeSerializer, ReviewSerializer
from employees.models import Employee, Review


class EmployeeListView(ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        employees = Employee.objects.all()
        return queryset_pagination(self.request, employees)


class EmployeeReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request):
        employee_id = request.POST.get('employee', None)
        employee = get_object_or_404(Employee, id=employee_id)
        name = request.POST.get('name', None)
        text = request.POST.get('text', None)
        rating = request.POST.get('rating', 5)
        review = model_to_dict(Review.objects.create(employee=employee, name=name, text=text, rating=rating))

        return JsonResponse(review, safe=False, json_dumps_params={'indent': 2})


class EmployeeDetailView(RetrieveAPIView):
    serializer_class = EmployeeSerializer

    def get(self, request, slug):
        employee = get_object_or_404(Employee, slug=slug)
        reviews = Review.objects.filter(employee=employee)
        reviews_list = []
        indx = 0
        for review in reviews:
            reviews_list.append(model_to_dict(review, fields=['name', 'text', 'rating']))
            reviews_list[indx].update({'publish_date': review.pub_date.strftime("%d %b %Y")})
            indx += 1
        data = model_to_dict(employee, fields=['name', 'position', 'type_of_works', 'slug'])
        data.update({'photo': request.build_absolute_uri(employee.photo.url)})
        data.update({'state': employee.state.name})
        data.update({'reviews': reviews_list})
        data.update({'seo': model_to_dict(employee.seo)})
        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


class EmployeeReviewList(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(employee__id=self.kwargs['id'])
