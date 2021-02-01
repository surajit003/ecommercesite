"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "admin_interface",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "django_countries",
    "phonenumber_field",
    "crispy_forms",
    "user.apps.AccountConfig",
    "catalog",
    "common",
    "cart",
    "order",
    "checkout",
    "payment",
    "vendor.apps.VendorConfig",
    "buyer",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
]

ROOT_URLCONF = "ecommerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "ecommerce.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DATABASE_NAME"),
        "USER": config("DATABASE_USERNAME"),
        "PASSWORD": config("DATABASE_PASSWORD"),
        "HOST": "localhost",  # Or an IP Address that your DB is hosted on
        "PORT": "3306",
        "ATOMIC_REQUESTS": True,
        "OPTIONS": {
            "sql_mode": "traditional",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/ecommerce/static/"
STATICFILES_DIRS = (
    os.path.join(
        BASE_DIR, "static"
    ),  # do not comment this line out as it renders the static files
)
MEDIA_ROOT = os.path.join(BASE_DIR, "static/media/upload/")
MEDIA_URL = os.path.join(BASE_DIR, "static/media/upload/")
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}
SITE_ID = 1

SESSION_COOKIE_NAME = "sessionid"
# The module to store sessions data.
SESSION_ENGINE = "django.contrib.sessions.backends.db"
# Age of cookie, in seconds (default: 2 weeks).
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2
# Whether a user's session cookie expires when the Web browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# Whether the session cookie should be secure (https:// only).
SESSION_COOKIE_SECURE = False
RABBITMQ_BROKER_URL = config("BROKER_URL")
RABBITMQ_USERNAME = config("BROKER_USERNAME")
RABBITMQ_PASSWORD = config("BROKER_PASSWORD")
RABBITMQ_PORT = config("BROKER_PORT", default="5672")
RABBITMQ_VHOST = config("BROKER_VHOST", default="pbp_main")
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND")
CELERY_WHISTLE_VHOST = config("CELERY_WHISTLE_VHOST")
CELERY_BROKER_URL = (
    f"pyamqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@"
    f"{RABBITMQ_BROKER_URL}/{CELERY_WHISTLE_VHOST}"
)

BROKER_URL = (
    f"pyamqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@"
    f"{RABBITMQ_BROKER_URL}/{RABBITMQ_VHOST}"
)

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]
X_FRAME_OPTIONS = "ALLOWALL"
CRISPY_TEMPLATE_PACK = "bootstrap4"
LOGIN_REDIRECT_URL = "/ecommerce/account/verify/user-type/"
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")
STRIPE_PUBLIC_KEY = config("STRIPE_PUBLIC_KEY")
ACCOUNT_LOGOUT_REDIRECT_URL = "/ecommerce/accounts/login/"
EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
SUPPORT_EMAIL = config("SUPPORT_EMAIL")
SERVER_URL = config("SERVER_URL")
