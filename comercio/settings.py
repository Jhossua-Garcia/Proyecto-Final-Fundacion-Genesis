
from pathlib import Path
import os

# Construye rutas dentro del proyecto de esta manera: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-!g08$pjbg2&$05nt$y5*tz0h%2vp(n^rw+g5sqg=6ovtv=ot5t'
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'categorias',
    'auths',
    'tienda',
    'carrito',
    #'cuentas',
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

ROOT_URLCONF = 'comercio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'categorias.context_processors.menu_links',
                'carrito.context_processors.contador_carrito',
            ],
        },
    },
]

WSGI_APPLICATION = 'comercio.wsgi.application'
AUTH_USER_MODEL = 'auths.Auth'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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
LANGUAGE_CODE = 'es-eu'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'


STATICFILES_DIRS = [
    BASE_DIR / "comercio/static",
]
STATIC_ROOT = BASE_DIR / "static"


#los archovos media
MEDIA_URL= '/media/'
MEDIA_ROOT= BASE_DIR /'media'

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.INFO: "",
    50: "critical",
}

#MI CONFIGURACION PARA VALIDAR LA CUENTA POR SMTP
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER ='codelatincolombia@gmail.com'
EMAIL_HOST_PASSWORD='qzbt vepo ggqi gmic'
EMAIL_USE_TLS= True
DEFAULT_FROM_EMAIL='codelatincolombia@gmail.com'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "Panel de Administración",
    "site_header": "LatinShop",
    "site_brand": "LatinShop",
    "site_logo": "images/logo2.jpg",
    "welcome_sign": "Bienvenido A LatinShop",
    "copyright": "Codelatin 2025",
    "show_ui_builder": True,
    "theme": "solar",  # Solo define un theme
    "dark_mode_theme": "superhero",
}