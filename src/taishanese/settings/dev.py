from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't7y6thl$b%nw=+voj&^%3ci_43&2vb1q0hc&7(r1f!gb4b4(9j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taishanese',
        'USER': 'blep',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}
