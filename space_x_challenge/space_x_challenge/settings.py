"""
Django settings for space_x_challenge project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-a2epr84uz0z#asq)ibp$@y6cf#=0kz2^a+8#y^iuj-dmiy+(c%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_rq",
    "trello_integration",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "space_x_challenge.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "space_x_challenge.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "space_x_challenge",
        "USER": "elon",
        "PASSWORD": "musk",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

if (
    "test" in sys.argv or "test_coverage" in sys.argv
):  # Covers regular testing and django-coverage
    DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3"}

RQ_QUEUES = {"default": {"HOST": "localhost", "PORT": 6379, "DB": 0}}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TRELLO_CONF = {
    "key": os.getenv("TRELLO_KEY"),
    "token": os.getenv("TRELLO_TOKEN"),
    "board_id": os.getenv("BOARD_ID", "5c964efa007d068f5d70116c"),
    "todo_list_id": os.getenv("BOARD_ID", "5c964f089b7c0644b67bcd16"),
    "research_label_id": os.getenv("RESEARCH_LABEL_ID", "62d7f8e8ed2bd4296fc93a92"),
    "test_label_id": os.getenv("TEST_LABEL_ID", "62d7f8ef7069b059fbabcb83"),
    "maintenance_label_id": os.getenv("MAINTENANCE_LABEL_ID", "62d7f9025e0a2576685ab70e"),
    "bug_label_id": os.getenv("BUG_LEVEL_ID", "62d82af0ae4ee51caf8bb105")
}
