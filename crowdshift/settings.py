"""
Django settings for crowdshift project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_ROOT = os.path.abspath(PROJECT_PATH)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "39ytrtfzb-$km7s^-4m7+32fl(@k1!)heltbdwe3z+qb*(c-e+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'registration',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reviews',
    'storages',
    'debug_toolbar',
    
)

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
SITE_ID = 1

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'crowdshift.urls'

WSGI_APPLICATION = 'crowdshift.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_postgrespool',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            #'NAME': 'd2one8uovq33oi',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            #'USER': 'aplvndlnovsejk',
            #'PASSWORD': 'TO7FLfsfGu4Q7HAev4gkrauflt',
            #'HOST': 'ec2-50-17-192-136.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            #'PORT': '5432',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Parse database configuration from $DATABASE_URL
#DATABASES['default'] =  dj_database_url.config()
DATABASES = {'default': dj_database_url.parse('postgres://aplvndlnovsejk:TO7FLfsfGu4Q7HAev4gkrauflt@ec2-50-17-192-136.compute-1.amazonaws.com:5432/d2one8uovq33oi')}
# Enable Connection Pooling (if desired)
DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAIQ4PMYG2GX2CVXGQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'crowdshift'
