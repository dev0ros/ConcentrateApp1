"""
Django settings for ConcentrateApp project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import posixpath
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yzfrelt1^n8)ux5c5*uedpw)80*%9d2ir_=1z(n_-^dncf)8@w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['concentrationapp1.azurewebsites.net','127.0.0.1','localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
   "whitenoise.runserver_nostatic",
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'concentrateapp_folder'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ConcentrateApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'concentrateapp_folder/templates']
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

WSGI_APPLICATION = 'ConcentrateApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATICFILES_DIRS = [
    BASE_DIR / "/concentrateapp_folder/static",
    #os.path.join(BASE_DIR, '../static'),
    # 'var/www/static/',
]
#STATIC_URL = '/static/'
VENV_PATH = os.path.dirname(BASE_DIR)
#STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')

STATIC_URL = os.environ.get("DJANGO_STATIC_URL", "/static_root/")
STATIC_ROOT = os.environ.get("DJANGO_STATIC_ROOT", "./static_root/")
# ???????????? ?????????????? ???????? ???????? ???????????? ?????????? F
#STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')
#STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))'''

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'