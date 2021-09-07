from django.urls import path
from services.api.views import ServicesListView, ServicesDetailView, ServiceCategoryView, ServiceCategoryListView

app_name = 'services_api'


urlpatterns = [
    path('services/', ServicesListView.as_view(), name='services-list'),
    path('services/categories/', ServiceCategoryListView.as_view(), name='service-categories'),
    path('services/category/<slug:slug>/', ServiceCategoryView.as_view(), name='services-in-category'),
    path('services/<slug:slug>/', ServicesDetailView.as_view(), name='services-detail'),
]
