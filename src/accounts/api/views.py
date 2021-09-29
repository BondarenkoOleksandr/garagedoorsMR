from urllib.parse import urlencode

from django.contrib.auth.models import User
from rest_framework.views import APIView

from django.urls import reverse
from django.shortcuts import redirect

from accounts.utils import google_get_access_token, google_get_user_info, jwt_login


class GoogleLoginApi(APIView):

    def get(self, request, *args, **kwargs):

        code = request.GET.get('code')
        error = request.GET.get('error')

        login_url = f'http://localhost:8008/login'

        if error or not code:
            params = urlencode({'error': error})
            return redirect(f'{login_url}?{params}')

        domain = 'https://garagedoors.fun'
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

        response = redirect('https://garagedoors.fun/api/articles/')
        response = jwt_login(response=response, user=user)

        return response