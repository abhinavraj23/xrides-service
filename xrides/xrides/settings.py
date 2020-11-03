"""
Django settings for xrides project.

Generated by 'django-admin startproject' using Django 2.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i7pt=)en(052e6ebq3*ccxe*fdo0_qt%mpf$h4vm8f$x-tn7lf'

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
    'django_elasticsearch_dsl',
    'django_elasticsearch_dsl_drf',
    'rest_framework',
    'auditlog',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
]

ROOT_URLCONF = 'xrides.urls'

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

WSGI_APPLICATION = 'xrides.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'xrides_db',
        'USER': 'abhinavraj',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
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

# Log Conf
if not os.path.exists('log'):
    os.makedirs('log')

APP_LOG_FILENAME = os.path.join(BASE_DIR, 'log/app.log')

LOGFILE_SIZE = 20 * 1024 * 1024
LOGFILE_COUNT = 5
LOGFILE_APP = 'xrides'
LOGFILE_APP2 = 'api'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
            'datefmt' : "%d-%b-%Y %H:%M:%S"
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        },
        'applog': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': APP_LOG_FILENAME,
            'maxBytes': LOGFILE_SIZE,
            'backupCount': LOGFILE_COUNT,
            'formatter': 'standard',
        }
    },
    'loggers': {
        LOGFILE_APP: {
            'handlers': ['applog'],
            'level': 'INFO',
            'propagate': True,
        },
        LOGFILE_APP2: {
            'handlers': ['applog'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

# Elasticsearch

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': os.environ.get('ES_HOST', 'elasticsearch:9200'),
        'timeout': 30,
    },
}

from django_elasticsearch_dsl import Index

ES_INDEX = Index('bookings')  # Name of the Elasticsearch index

# See Elasticsearch Indices API reference for available settings
ES_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=0
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
