import dj_database_url
import os
from pathlib import Path


AUTH_USER_MODEL = 'registration.CustomUser'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-@00w4l=!ga8vk08b9p%%v8wz-qm$sx&v@^n!$ak@$$q8x+l9#3')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:3000/",
#     "http://localhost:3000/",

# ]

CORS_ALLOW_ALL_ORIGINS = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'api',
    'rest_framework',
    'rest_framework.authtoken',
    'flowrate',
    'location',
    'device',
    'temperature_recording', 
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'atembobackend.urls'

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

# Heroku settings.
import django_heroku
django_heroku.settings(locals())

WSGI_APPLICATION = 'atembobackend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

from decouple import config


# DATABASES = {
#     'default': {
#         'ENGINE': config('DB_ENGINE'),
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT', default='5432')
#     }
# }



DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

import logging
logging.basicConfig()
logger = logging.getLogger('django.db.backends')
logger.setLevel(logging.DEBUG)

# Internationalization
# https://docs.djangoproject.comse a Different Authentication Method: If the API uses CSRF tokens as a form of authentication, you can check if it supports other authentication methods, such as API keys, OAuth tokens, or basic authentication. If these alternatives are available, you can use them instead of dealing with CSRF tokens./en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SWAGGER_SETTINGS = { 
    'DEFAULT_AUTO_SCHEMA_CLASS': 'drf_yasg.inspectors.SwaggerAutoSchema',
    'DEFAULT_INFO': 'your_project.api_info',
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES':[
    'rest_framework.authentication.TokenAuthentication'
],}
