"""
Django settings for djangoProject project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^7e8i2pc7x1=zl8@#f(lt208--94a6!r)u71a5ou^#1!b)(xxd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '127.0.0.1', '0.0.0.0', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'codecapstest'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'djangoProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

import dj_database_url
import dj_mongo_database_url

db_url = os.environ.get("DATABASE_URL", False)

os_mongo_url = os.environ.get("DATABASE_URL")
parsed_dj_mongo_url = dj_mongo_database_url.parse(os.environ.get("DATABASE_URL"))
dj_mongo_url = {}
dj_mongo_url["ENGINE"] = 'djongo'
dj_mongo_url["HOST"] = parsed_dj_mongo_url['HOST']
dj_mongo_url["NAME"] = parsed_dj_mongo_url['NAME']
dj_mongo_url["ENFORCE_SCHEMA"] = False
dj_mongo_url['CLIENT'] = {
    'host': parsed_dj_mongo_url['HOST'],
    'port': 27017,
    'username': parsed_dj_mongo_url['USER'],
    'password': parsed_dj_mongo_url['PASSWORD'],
    'authSource': 'admin',
    'authMechanism': 'SCRAM-SHA-256'
}
if db_url:
    DATABASES = {
        'default':  dj_mongo_url,
    }
else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )


# print(STATIC_ROOT)
#
print(PROJECT_ROOT)

print(f'Using DATABASE_URL: {os.environ.get("DATABASE_URL", "Using temp SQLite. Bind a mongo data capsule in the config tab to use it.")}')
print(f'Using TEXTFILE_URL: {os.environ.get("TEXTFILE_URL", "DjangoTestWriteFile.txt on temporary filesystem. Bind a storage Data capsule in the config tab to use it.")}')