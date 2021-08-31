from django.urls import path

from employees.api.views import EmployeeListView, EmployeeReviewCreateAPIView, EmployeeDetailView, EmployeeReviewList

app_name = 'employees_api'

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employees-list'),
    path('employee/<int:id>/', EmployeeDetailView.as_view(), name='single-employee'),
    path('employee/create_review/', EmployeeReviewCreateAPIView.as_view(), name='create-employee-review'),
    path('employee/<int:id>/get_reviews/', EmployeeReviewList.as_view(),name='get-reviews')
]
