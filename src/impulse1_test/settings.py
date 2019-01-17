"""
Local Developer Settings
"""

from .settings_base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ppye-i9vea9qw8+3^r+tpy92agkvyg(#855q^p!w09jwq$zi&_'


DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ['null']