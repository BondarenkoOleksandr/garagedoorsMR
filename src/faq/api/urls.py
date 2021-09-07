from django.urls import path

from faq.api.views import FAQListView, FAQByServiceView

app_name = 'faq_api'

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faqs-list'),
    path('faqs/<int:id>/', FAQByServiceView.as_view(), name='faqs-list'),
]
