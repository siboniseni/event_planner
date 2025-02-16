"""Django settings for the event_planner project.

This file contains the default configuration for the event_planner Django project.

It was generated by 'django-admin startproject' using Django 5.1.4 and includes:

- Security-related settings (SECRET_KEY, DEBUG, ALLOWED_HOSTS)
- Application definition and installed apps
- Middleware configuration
- URL resolution via ROOT_URLCONF
- Templates configuration
- Database settings
- Password validation rules
- Internationalization and timezone settings
- Static and media file handling

For more details:
    https://docs.djangoproject.com/en/5.1/topics/settings/
    https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
# URL to access static files
STATIC_URL = '/static/'

# Directory where static files will be collected
STATIC_ROOT = BASE_DIR / "staticfiles"

# Additional directories to look for static files during development
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mms2&o-@=-(xf&uue#hrvtwz#y-75g)!ghad@-vjldpa_6=wje'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['eventplanner.com', 'www.eventplanner.com', '127.0.0.1', 'event-planner-2025-7b214c2805eb.herokuapp.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'events',
    'user_auth',
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

ROOT_URLCONF = 'event_planner.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'event_planner.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files (Uploaded content)
MEDIA_URL = '/media/'  # URL prefix for serving media files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory where uploaded files will be saved

LOGIN_URL = '/user_auth/login/'



