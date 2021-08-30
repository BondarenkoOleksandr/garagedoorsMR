from rest_framework.generics import ListAPIView

from employees.api.serializers import EmployeeSerializer
from employees.models import Employee


class EmployeesListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer