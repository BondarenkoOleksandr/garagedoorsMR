from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '185.233.117.122', 'garagedoors.fun', 'vps-38133.vps-default-host.net']

MEDIA_ROOT = '/var/www/gdr_mr/media'
STATIC_ROOT = '/var/www/gdr_mr/static'
