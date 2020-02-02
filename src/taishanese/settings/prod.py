"""Settings used in production environment."""

from .base import *
import dj_database_url

# TODO: set to something once domain finalized
ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ['SECRET_KEY']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
