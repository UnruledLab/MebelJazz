# -*- coding: utf-8 -*-
"""
Django settings for mebeljazz project.

Generated by 'django-admin startproject' using Django 1.9.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from __future__ import unicode_literals

import os

from django.utils.translation import ugettext_lazy as _

from oscar import get_core_apps
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar.defaults import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'arr#1^4y$%1o*u&p%z^8)bn6mlzw+@sykv&99iqw^cc!8my+yi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',

    'compressor',
    'widget_tweaks',
    'ckeditor',
    'constance',
    'constance.backends.database',
    'nested_admin',

    'slider',
    'articles',
    'site_reviews',
    'common',
    'filter',
    'favoritelist',
    'banner',
    'apps.catalogs',
] + get_core_apps(['apps.promotions', 'apps.catalogue', 'apps.catalogue.reviews', 'apps.basket', 'apps.order', 'apps.checkout', 'apps.partner'])

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'favoritelist.middleware.FavoriteListMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'mebeljazz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            OSCAR_MAIN_TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
                'constance.context_processors.config',
            ],
        },
    },
]

WSGI_APPLICATION = 'mebeljazz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mebeljazz',
        'USER': 'mebeljazz',
        'PASSWORD': 'mebeljazz',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#################################################################
# Haystack settings

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        'EXCLUDED_INDEXES': ['oscar.apps.search.search_indexes.ProductIndex']
    },
}

#################################################################
# Ckeditor settings

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
            'toolbar_Custom': [
                {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
                        '-', 'Undo', 'Redo'
                    ]
                },
                {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', '-', 'RemoveFormat']},
                {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-',
                                    'Outdent', 'Indent', '-',
                                    'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-',
                                    'Blockquote']},
                {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
                {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar']},
                {'name': 'styles', 'items': ['Styles', 'Format']},
                {'name': 'editing', 'items': ['Scayt']},
                {'name': 'tools', 'items': ['Maximize']},
                {'name': 'document', 'items': ['Source']}
        ]
    }
}


DJANGO_WYSIWYG_FLAVOR = "ckeditor"

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    'CONTACT_NUM_1': ('(066) 124 47 94', u'Телефон 1'),
    'CONTACT_NUM_2': ('(093) 552 51 00', u'Телефон 2'),
    'CONTACT_NUM_3': ('(068) 678 70 66', u'Телефон 3'),
    'CONTACT_EMAIL': ('info@mebeljazz.com.ua', u'Почта'),
    'EMAIL_FOR_BLANC': ('info@mebeljazz.com.ua', u'Почта для оповещений'),
    'ADDRESS': (u'г. Киев, ул. Кириловская 86', u'Адрес'),
}

#################################################################

USE_DJANGO_JQUERY = False

WKHTMLTOPDF_CMD = '/usr/bin/wkhtmltopdf'

#################################################################
# OSCAR settings

OSCAR_DEFAULT_CURRENCY = 'UAH'

OSCAR_SEARCH_FACETS = {
    'fields': OrderedDict([
        ('product_class', {'name': _('Type'), 'field': 'product_class'}),
        ('rating', {'name': _('Rating'), 'field': 'rating'}),
    ]),
    'queries': OrderedDict([
        ('price_range',
         {
             'name': _('Price range'),
             'field': 'price',
             'queries': [
                 # This is a list of (name, query) tuples where the name will
                 # be displayed on the front-end.
                 (_('0 to 20'), u'[0 TO 20]'),
                 (_('20 to 40'), u'[20 TO 40]'),
                 (_('40 to 60'), u'[40 TO 60]'),
                 (_('60+'), u'[60 TO *]'),
             ]
         }),
    ]),
}

THUMBNAIL_QUALITY = 60


try:
    from local_settings import *
except ImportError:
    pass
