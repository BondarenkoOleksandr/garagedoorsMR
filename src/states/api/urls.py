from django.urls import path

from states.api.views import StateListView, StateDetailView

app_name = 'states_api'

urlpatterns = [
    path('states/', StateListView.as_view(), name='states-list'),
    path('states/<slug:slug>/', StateDetailView.as_view(), name='states-list'),

]
