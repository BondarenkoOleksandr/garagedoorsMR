from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

MEDIA_ROOT = '/var/www/gdr_mr/media'
STATIC_ROOT = '/var/www/gdr_mr/static'
