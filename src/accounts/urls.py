from django.urls import path

from accounts.views import GoogleLoginView

app_name = 'accounts'

urlpatterns = [
    path('', GoogleLoginView.as_view(), name='google-login'),
]