"""
Django settings for temp_axes_try project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from datetime import timedelta
from django.apps.config import AppConfig

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&4g&msjq*jjy%2(*^+fkkxgb2xlres#nq*s7g7d@zed2@$q5_='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'axes',
]

MIGRATION_MODULES = {AppConfig.create(entry).label: None for entry in INSTALLED_APPS}

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'temp_axes_try.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'temp_axes_try.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


# Feature Flag to enable/disable Axes
AXES_ENABLED = True
# Env variables to configure Axes
AXES_CACHE = os.environ.get("AXES_CACHE", "")
AXES_LOCK_OUT_AT_FAILURE = False
# # AXES Global configuration
AXES_FAILURE_LIMIT = 100
AXES_COOLOFF_TIME = timedelta(minutes=5)
AXES_ONLY_ADMIN_SITE = False
AXES_ONLY_USER_FAILURES = False
AXES_ENABLE_ADMIN = False
AXES_LOCK_OUT_BY_USER_OR_IP = False
AXES_USERNAME_FORM_FIELD = "username"
AXES_USERNAME_CALLABLE = None
AXES_PROXY_ORDER = "left-most"
AXES_PROXY_COUNT = None
AXES_PROXY_TRUSTED_IPS = None
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = False
AXES_USE_USER_AGENT = False
# AXES_LOGGER = "axes.watch_login"
AXES_VERBOSE = True
AXES_NEVER_LOCKOUT_GET = False
AXES_NEVER_LOCKOUT_WHITELIST = True
AXES_ONLY_WHITELIST = False
AXES_WHITELIST_CALLABLE = None
AXES_IP_WHITELIST = None
AXES_IP_BLACKLIST = False
AXES_RESET_ON_SUCCESS = True
AXES_HANDLER = "axes.handlers.cache.AxesCacheHandler"
AXES_META_PRECEDENCE_ORDER = (
    "HTTP_X_REAL_IP",
    "REMOTE_ADDR",
)
