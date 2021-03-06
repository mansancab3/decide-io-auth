"""
Django settings for decide project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import django_heroku


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^##ydkswfu0+=ofw0l#$kv^8n)0$i(qd&d&ol#p9!b$8*5%j1+'

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
    'corsheaders',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'social_django',
    'crispy_forms',

    #Authentification with Twitter and Google
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.google',


    #FInAuthentification with Twitter and Google
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID=1

ACCOUNT_LOGOUT_ON_GET = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

AUTHENTICATION_BACKENDS = [
    'base.backends.AuthBackend',
    'django_facebook.auth_backends.FacebookBackend' ,
    'django.contrib.auth.backends.ModelBackend' ,
    #ojcndjcnsdjcsndjcnsjscjsdn
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.twitter.TwitterOAuth',
   #  'social.backends.twitter.TwitterOAuth',

    #sojcndocsdosnocnsdocnsd
]

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
#SOCIAL_AUTH_LOGOUT_REDIRECT_URL = '/accounts/logout'

SOCIAL_AUTH_LOGIN_URL = '/accounts/google/login/callback/'
SOCIAL_URL_REDIRECT = '/admin/login'
LOGIN_REDIRECT_URL = '/index' #Cambiar para página logeada.
LOGOUT_REDIRECT_URL = '/accounts/login'

#LOGIN_URL = '/login'
#LOGIN_REDIRECT_URL = '/authentication/editUser'





SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',  # <--- este
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)



MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

SOCIAL_AUTH_TWITTER_KEY = 'NaY7zW7Q9pZZuH0XOkgLBacem'
SOCIAL_AUTH_TWITTER_SECRET = 'xvIQeBIfaH2SJ3TxiN1UiMdLI1GKDetp9weGUVWA1XQsGHlwr9'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1096255128002-nbae62sdmoo0v19ugua198ou30coht1s.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '--qvDJeFXlaKDTWtO2felsXu'


BASEURL = 'https://decide-io-authentication.herokuapp.com'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#sichsdifbijcbsijcsncjnsdcps
   # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',

#iuchsdcbsducbsdicbspibspdicds

]


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)


ROOT_URLCONF = 'decide.urls'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'authentication/templates'),
)

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
                # `allauth` needs this from django
                'django.template.context_processors.request',
                'django_facebook.context_processors.facebook',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                #scscfcsvfdvdfvdfvdfvdfvdfv
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                #vdfvdvdfvdfvdvdfvdf

            ],
        },
    },
]

WSGI_APPLICATION = 'decide.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256

try:
    from local_settings import *
except ImportError:
    print("local_settings.py not found")


SOCIAL_AUTH_FACEBOOK_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email'
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
]

AUTH_PROFILE_MODULE = 'authentication.Profile'



INSTALLED_APPS = INSTALLED_APPS + MODULES
django_heroku.settings(locals())

#Variables necesarias para que mande correo de confirmacion
EMAIL_HOST='smtp.live.com'
EMAIL_HOST_USER= 'decideio@hotmail.com'
EMAIL_HOST_PASSWORD= 'pepibami1'
EMAIL_PORT= 587
EMAIL_USE_TLS= True

#Key privada de google captcha
GOOGLE_RECAPTCHA_SECRET_KEY = '6Lfly4wUAAAAANwEGC6WImTeZqQ74YZxP_-eA8ri'
APIS = {}