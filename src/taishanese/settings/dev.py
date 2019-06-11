"""Settings used in dev environment."""

from .base import *
import dj_database_url

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=False)
