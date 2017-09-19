#-*- coding: utf-8 -*-
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7fcgy8tuxr19ct-0q076ja2ca#ai+7a&v-$10h)3q)bx2vozff'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'http://localhost:8080']

# Application definition
INSTALLED_APPS = [
    'flat_responsive',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'direcciones',
]

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Lo cambiamos aqui
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'examendjango.urls'

TEMPLATES = [
    {  # Motor de Templates Jinja =============================================
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': ['%s/templates/' % (PROJECT_DIR), 'direcciones/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'examendjango.jinja.env.JinjaEnvironment',
            'extensions': [
                    'jdj_tags.extensions.DjangoCompat',
                    'jinja2.ext.i18n',
                    'jinja2.ext.with_',
                    'jinja2.ext.autoescape'
                ]
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '%s/templates/' % (PROJECT_DIR),
            '%s/templates/registration/' % (PROJECT_DIR),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                # add this processor
            ],
        },
    },
]

WSGI_APPLICATION = 'examendjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'examen',
        'USER': 'sl',
        'PASSWORD': 'qwerty',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/--------------------------
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'es-MX'

ugettext = lambda s: s  # Funcion simuladora
#Lenguaje preferido por el usuario actual
LANGUAGES = (
    ('es', ugettext('Spanish')),
    ('en', ugettext('English')),
)

# Definimos la ruta de los archivos de idiomas
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

TIME_ZONE = 'America/Mexico_City'
USE_TZ = True
#------------------------------------------------------------------------------

# Static files (CSS, JavaScript, Images)
#STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

#Media files ------------------------------------------------------------------
MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'