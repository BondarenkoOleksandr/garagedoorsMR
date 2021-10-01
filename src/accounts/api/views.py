from urllib.parse import urlencode

from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.views import APIView

from django.urls import reverse
from django.shortcuts import redirect

from accounts.models import UserProfile
from accounts.utils import google_get_access_token, google_get_user_info, jwt_login, save_avatar, \
    facebook_get_access_token, facebook_get_user_info
from app.settings import base
from core.utils import get_user_by_jwt


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
        user_profile, _ = UserProfile.objects.get_or_create(user=user)
        save_avatar(user_profile, user_data)

        response = redirect(base.DOMAIN)
        response = jwt_login(response=response, user=user)

        return response


class FacebookLoginApi(APIView):

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        error = request.GET.get('error')

        login_url = base.DOMAIN + '/login'

        if error or not code:
            params = urlencode({'error': error})
            return redirect(f'{login_url}?{params}')

        domain = base.DOMAIN
        api_uri = reverse('accounts_api:facebook-login')
        redirect_uri = f'{domain}{api_uri}'

        access_token = facebook_get_access_token(code=code, redirect_uri=redirect_uri)
        print(access_token)

        user_data = facebook_get_user_info(access_token=access_token)
        print(user_data)

        profile_data = {
            'username': user_data['email'].split('@')[0],
            'email': user_data['email'],
            'first_name': user_data.get('first_name', ''),
            'last_name': user_data.get('last_name', ''),
        }

        # We use get-or-create logic here for the sake of the example.
        # We don't have a sign-up flow.
        user, _ = User.objects.get_or_create(**profile_data)
        user_profile, _ = UserProfile.objects.get_or_create(user=user)
        save_avatar(user_profile, user_data)

        response = redirect(base.DOMAIN)
        response = jwt_login(response=response, user=user)
        print(response.cookies['token'])

        return response


class GetMeApi(APIView):
    def get(self, request, *args, **kwargs):
        user = get_user_by_jwt(request)

        if isinstance(user, User):
            user = UserProfile.objects.filter(user=user)
            print(user)
            user = user.values('user__username', 'user__first_name', 'user__last_name', 'image')
            print(user)
            for usr in user:
                usr.update(
                    {
                     'image': request.scheme + '://' + request.get_host() + '/' + base.MEDIA_URL + usr['image'],
                     })

            data = list(user)

            return JsonResponse(user, safe=False)

        else:
            return JsonResponse(user[0], status=400, safe=False)
