"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%!d^ujioyx2&sp+7(9sm*t%n^ma8raqdx%w1ddozviw!-d0*9c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    # "http://localhost:8000",
    # "http://127.0.0.1:8000"
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    "rest_framework_simplejwt.token_blacklist",
    # Local App
    'bvs.apps.BvsConfig',
    'bvs.user.apps.UserConfig',
    'bvs.auth.apps.AuthConfig',
    'bvs.patient.apps.PatientConfig',
    'bvs.treatment.apps.TreatmentConfig',
    'bvs.donor.apps.DonorConfig',
    'bvs.occupation.apps.OccupationConfig',
    'bvs.ethnic.apps.EthnicConfig',
    'bvs.hospital.apps.HospitalConfig',
    'bvs.language.apps.LanguageConfig',
    'bvs.educationlevel.apps.EducationlevelConfig',
    'bvs.religion.apps.ReligionConfig',
    'bvs.family.apps.FamilyConfig',
    'bvs.funding.apps.FundingConfig',
    'bvs.pshychosocial.apps.PshychosocialConfig',
    'bvs.physiotherapy.apps.PhysiotherapyConfig',
    'bvs.burncause.apps.BurncauseConfig',
    'bvs.burntype.apps.BurntypeConfig',
    'bvs.dashboard.apps.DashboardConfig',
    'bvs.question.apps.QuestionConfig',
    'bvs.reintegration.apps.ReintegrationConfig',
    'bvs.followUpSummary.apps.FollowupsummaryConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bvs3',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# default auth model
AUTH_USER_MODEL = 'bvs_user.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS':
        ['django_filters.rest_framework.DjangoFilterBackend'],

    # 'DEFAULT_PAGINATION_CLASS':
    #     'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 3,

}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_AFTER_INACTIVITY': timedelta(days=7),
    'SLIDING_TOKEN_REFRESH_SLIDING_WINDOW': timedelta(days=2),
    'SLIDING_TOKEN_REFRESH_ON_LOGIN': True,
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "uploads"

# Default avatar URL

DEFAULT_AVATAR_URL = "https://avatars.dicebear.com/api/identicon/.svg"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'mail.bvsnepal.org'
# EMAIL_PORT = 465
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'admin@bvsnepal.org'
# EMAIL_HOST_PASSWORD = '@dminBvs'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'xxxx.dipen@gmail.com'
EMAIL_HOST_PASSWORD = 'xxxx xxxx xxxx xxxx'
