
import os
import dj_database_url
from pathlib import Path
import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dnxh+)lu1zwisb#_mb3n$0qey_y!f1hmb5d+)ellr@+&c!a8wh'

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
    'users',
    'dashboard',
    'companydashboard',
    'reviews',
    'catergory',
    'storages',
    'main',
    'rest_framework',
    'api',

]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'templates')
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}
# DATABASES['default'] = dj_database_url.config(
#     conn_max_age=600, ssl_require=True)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, "images/")


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

EMAIL_BACKEND = 'django_ses.SESBackend'
DEFAULT_FROM_EMAIL = 'info@kleui.com'
AWS_ACCESS_KEY_ID = 'AKIAQVPXYDDKO66DFQWP'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'business-financial-reviews'
AWS_SES_REGION_NAME = 'us-east-1'  # (ex: us-east-2)
AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = None

# s3 static settings

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
AWS_S3_FILE_OVERWRITE = False

AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AUTH_USER_MODEL = 'users.CustomUser'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())
