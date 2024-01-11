"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-92p3roix#can--*vpx)%a036)54+&=mh9u5pkz%u!g)pd@53v$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
AUTH_USER_MODEL = 'authentication.CustomUser'

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'authentication',
    'book',
    'news',
]

REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': [
       'rest_framework.authentication.TokenAuthentication',
   ],

}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

JAZZMIN_SETTINGS = {
    "site_title": "Bookshelf Admin",
    "site_header": "Bookshelf",
    "site_brand": "Bookshelf",
    "site_logo_classes": "img-circle",
    "welcome_sign": "Welcome to the Bookshelf",
    "copyright": "Bookshelf. Developed by Group 3 during the Tuwaiq Academy Final Project",
    "user_avatar": None,
    "login_logo": None,
    "login_logo_dark": None,
    "site_icon": None,
    "user_avatar": None,
    "search_model": ["authentication.CustomUser","book.Book"],

    
    
    "topmenu_links": [

        {"name": "Dashboard", "url": "/admin", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/FMashi/DRFBookshelf", "new_window": True},
        {"model": "auth.User"},
        {"app": "book"},
        {"app": "authentication"},
    ],
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/FMashi/DRFBookshelf", "new_window": True},
        {"model": "auth.user"},
        {"model": "auth.Group"}
    ],


    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": ["auth.group","auth.user"],

    "order_with_respect_to": [
        "auth",
        "book",
        "authentication",
        "news",
        
        "authentication.Cities",
        "authentication.Semesters",
        "authentication.Desposites",
        "authentication.CustomUser",
        "authentication.Profile",
    
        "book.Author",
        "book.Publisher",
        "book.Faculty",
        "book.Libraries",
        "book.Language",
        "book.Category",
        "book.Section",
        "book.Book",
        "book.EBook",
        "book.Copy",
        "book.model",
        ],
    
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "authtoken.tokenproxy": "fas fa-key",
        "authentication.Cities": "fas fa-city",
        "authentication.Semesters": "fas fa-calendar-alt",
        "authentication.Desposites": "fas fa-piggy-bank",
        "authentication.CustomUser": "fas fa-user-cog",
        "authentication.Profile": "fas fa-id-card",
        "book.Author": "fas fa-pen",  
        "book.Publisher": "fas fa-building",  
        "book.Faculty": "fas fa-university", 
        "book.Libraries": "fas fa-book",  
        "book.Language": "fas fa-language",
        "book.Category": "fas fa-bookmark",
        "book.Section": "fas fa-layer-group",
        "book.Book": "fas fa-book",
        "book.EBook": "fas fa-file-alt",
        "book.Copy": "fas fa-copy",
        "book.model": "fas fa-cogs",
        "news.News": "fas fa-newspaper"
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "use_google_fonts_cdn": True,
}


