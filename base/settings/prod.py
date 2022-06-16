from .base import *

import django_heroku
import dj_database_url

django_heroku.settings(locals())

DATABASES['default'] = dj_database_url.config()
DEBUG = False
ALLOWED_HOSTS = ['fadi-rezek-salloum.herokuapp.com']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True