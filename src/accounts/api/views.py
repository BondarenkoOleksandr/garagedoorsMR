from urllib.parse import urlencode

from django.contrib.auth.models import User
from rest_framework.views import APIView

from django.urls import reverse
from django.shortcuts import redirect

from accounts.models import UserProfile
from accounts.utils import google_get_access_token, google_get_user_info, jwt_login, save_avatar
from app.settings import base


class GoogleLoginApi(APIView):

    def get(self, request, *args, **kwargs):

        code = request.GET.get('code')
        error = request.GET.get('error')

        login_url = base.DOMAIN + '/login'

        if error or not code:
            params = urlencode({'error': error})
            return redirect(f'{login_url}?{params}')

        domain = base.DOMAIN
        api_uri = reverse('accounts_api:google-login')
        redirect_uri = f'{domain}{api_uri}'

        access_token = google_get_access_token(code=code, redirect_uri=redirect_uri)

        user_data = google_get_user_info(access_token=access_token)

        profile_data = {
            'username': user_data['email'].split('@')[0],
            'email': user_data['email'],
            'first_name': user_data.get('given_name', ''),
            'last_name': user_data.get('family_name', ''),
        }

        # We use get-or-create logic here for the sake of the example.
        # We don't have a sign-up flow.
        user, _ = User.objects.get_or_create(**profile_data)
        user_profile = UserProfile.objects.get_or_create(user=user)
        save_avatar(user_profile, user_data)


        response = redirect(base.DOMAIN)
        response = jwt_login(response=response, user=user)

        return response
