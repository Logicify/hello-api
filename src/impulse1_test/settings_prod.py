"""
Production Environment Settings
"""
import dj_database_url

from .settings_base import *


SECRET_KEY = os.environ['SECRET_KEY']


DEBUG = False

# should be restricted on reverse proxy
# https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/#allowed-hosts
ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': dj_database_url.config(env='DB_URL')
}


EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'alerts@impuls1.de')

EMAIL_SUBJECT_PREFIX = os.environ.get('EMAIL_SUBJECT_PREFIX', 'Logicify Microservice PROD: ')
ADMINS = [
    ('Microservice Alerts', 'microserice-alerts@logicify.domain'),
]


STATIC_ROOT = os.environ.get('STATIC_ROOT', '/srv/static')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/srv/media')
FILE_UPLOAD_PERMISSIONS = 0o644


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


CORS_ORIGIN_WHITELIST = os.environ.get('CORS_ORIGIN_WHITELIST', '').split(',')
