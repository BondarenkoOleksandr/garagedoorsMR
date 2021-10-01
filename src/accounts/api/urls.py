from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token

from accounts.api.views import GoogleLoginApi, FacebookLoginApi, GetMeApi

app_name = 'accounts_api'

urlpatterns = [
    path('login/google/', GoogleLoginApi.as_view(), name='google-login'),
    path('me/', GetMeApi.as_view(), name='me'),
    path('login/facebook/', FacebookLoginApi.as_view(), name='facebook-login'),
    path('token-refresh/', refresh_jwt_token),  # REFRESH JET TOKEN
    path('token-verify/', verify_jwt_token),  # VERIFY JET TOKEN
]