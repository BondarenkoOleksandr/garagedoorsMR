import random
from io import BytesIO
from typing import Dict, Any

import requests
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile
from django.http import HttpResponse
from rest_framework_jwt.settings import api_settings

from accounts.services import user_record_login
from app.settings import base


def google_get_access_token(*, code: str, redirect_uri: str) -> str:
    # Reference: https://developers.google.com/identity/protocols/oauth2/web-server#obtainingaccesstokens
    data = {
        'code': code,
        'client_id': base.GOOGLE_OAUTH2_CLIENT_ID,
        'client_secret': base.GOOGLE_OAUTH2_CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }

    response = requests.post(base.GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=data)

    if not response.ok:
        raise ValidationError('Failed to obtain access token from Google.')

    access_token = response.json()['access_token']

    return access_token


def google_get_user_info(*, access_token: str) -> Dict[str, Any]:
    # Reference: https://developers.google.com/identity/protocols/oauth2/web-server#callinganapi
    response = requests.get(
        base.GOOGLE_USER_INFO_URL,
        params={'access_token': access_token}
    )

    if not response.ok:
        raise ValidationError('Failed to obtain user info from Google.')

    return response.json()


def jwt_login(*, response: HttpResponse, user: User) -> HttpResponse:
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    response.set_cookie('token', token)

    user_record_login(user=user)

    return response


def save_avatar(profile, user_data):
    try:
        response = requests.get(user_data['picture'])
    except:
        response = requests.get(user_data['picture']['data']['url'])
    profile.image.save(user_data['email'].split('@')[0] + str(random.randint(1, 1000000000)) + '.jpg',
                       ImageFile(BytesIO(response.content)))
    profile.save()


def facebook_get_access_token(*, code: str, redirect_uri: str) -> str:
    # Reference: https://developers.google.com/identity/protocols/oauth2/web-server#obtainingaccesstokens
    data = {
        'code': code,
        'client_id': base.FACEBOOK_OAUTH2_CLIENT_ID,
        'client_secret': base.FACEBOOK_OAUTH2_CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }

    response = requests.post(base.FACEBOOK_ACCESS_TOKEN_OBTAIN_URL, data=data)

    if not response.ok:
        raise ValidationError('Failed to obtain access token from Facebook.')

    access_token = response.json()['access_token']

    return access_token


def facebook_get_user_info(*, access_token: str) -> Dict[str, Any]:
    # Reference: https://developers.google.com/identity/protocols/oauth2/web-server#callinganapi
    short_info = requests.get(
        base.FACEBOOK_USER_SHORT_INFO_URL,
        params={'access_token': access_token}
    )

    if not short_info.ok:
        raise ValidationError('Failed to obtain user info from Facebook.')

    response = requests.get(
        base.FACEBOOK_USER_FULL_INFO_URL + short_info.json()['id'],
        params={'access_token': access_token,
                'fields': 'first_name,last_name,picture,email'
                }
    )

    return response.json()
