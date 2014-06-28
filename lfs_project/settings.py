# python imports
import os

# django imports
from django.utils.translation import gettext_lazy as _

DIRNAME = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TESTING = False
THUMBNAIL_DEBUG =True

SWITCH = True


DEFAULT_FROM_EMAIL = 'your_email@domain.com'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = DIRNAME + "/media"

# static files settings
#STATIC_URL = '/static/'
#STATIC_ROOT = DIRNAME + "/sitestatic"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
# Need to be changed when publish
SECRET_KEY = '+0zsw5n@v7*rhl6r6ufqhoc6jlqq0f-u8c+gh(hjb+_jmg@rh6'



# Django 1.3.1
# # List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.load_template_source',
#     'django.template.loaders.app_directories.load_template_source',
# #     'django.template.loaders.eggs.load_template_source',
# )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',    
)

# Django 1.4.5
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'lfs.utils.middleware.RedirectFallbackMiddleware',
    "pagination.middleware.PaginationMiddleware",
)

ROOT_URLCONF = 'lfs_project.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (    
    "lfs_project.mytheme",
    #"lfs_project.lfs.catalog",
    'lfs_project.lfs.portlet',
    "lfstheme",
    "compressor",
    "django.contrib.admin",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "django.contrib.flatpages",
    "django.contrib.redirects",
    "django.contrib.sitemaps",
    'django_countries',    
    "pagination",
    'reviews',
    "tagging",
    "portlets",
    "lfs",
    "lfs.tests",
    'lfs.core',
    'lfs.caching',
    'lfs.cart',
    'lfs.catalog',
    'lfs.checkout',
    "lfs.criteria",
    "lfs.customer",
    "lfs.discounts",
    "lfs.export",
    'lfs.gross_price',
    'lfs.integrationtests',
    'lfs.mail',    
    'lfs.manage',
    'lfs.marketing',
    'lfs.manufacturer',
    'lfs.net_price',
    'lfs.order',
    'lfs.page',
    'lfs.payment',
    #'lfs.portlet',
    'lfs.search',
    'lfs.shipping',
    'lfs.supplier',
    'lfs.tagging',
    'lfs.tax',
    "lfs.customer_tax",
    'lfs.utils',
    'lfs.voucher',
    'lfs_contact',
    "lfs_order_numbers",
    'postal',
    'paypal.standard.ipn',
    'paypal.standard.pdt',
    'south',
    'hvad',
    'paintstore',
    'image_cropping',
    'easy_thumbnails',
    'lfs_project.django_carousel',    
)

if not DEBUG:
    INSTALLED_APPS +=('storages',)

FORCE_SCRIPT_NAME=""
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/manage/"

# Django 1.3.1
# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.core.context_processors.debug',
#     'django.core.context_processors.auth',
#     'django.core.context_processors.request',
#     'django.core.context_processors.media',
#     'django.core.context_processors.static',
#     'lfs.core.context_processors.main',
# )

# Django 1.4.5
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'lfs.core.context_processors.main',
)

AUTHENTICATION_BACKENDS = (
    'lfs.customer.auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# For sql_queries
INTERNAL_IPS = (
    "127.0.0.1",
)

CACHE_MIDDLEWARE_KEY_PREFIX = "lfs"
# CACHE_BACKEND = 'file:///'
# CACHE_BACKEND = 'locmem:///'
# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
#CACHE_BACKEND = 'dummy:///'

# Cache backend for django 1.4.5
CACHES = {'default': {
 'BACKEND':'django.core.cache.backends.locmem.LocMemCache',
}}

EMAIL_HOST = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

PAYPAL_RECEIVER_EMAIL = "info@yourbusiness.com"
PAYPAL_IDENTITY_TOKEN = "set_this_to_your_paypal_pdt_identity_token"

# TODO: Put this into the Shop model
LFS_PAYPAL_REDIRECT = True
LFS_AFTER_ADD_TO_CART = "lfs_added_to_cart"
LFS_RECENT_PRODUCTS_LIMIT = 5

LFS_ORDER_NUMBER_GENERATOR = "lfs_order_numbers.models.OrderNumberGenerator"
LFS_DOCS = "http://docs.getlfs.com/en/latest/"

LFS_INVOICE_COMPANY_NAME_REQUIRED = False
LFS_INVOICE_EMAIL_REQUIRED = True
LFS_INVOICE_PHONE_REQUIRED = True

LFS_SHIPPING_COMPANY_NAME_REQUIRED = False
LFS_SHIPPING_EMAIL_REQUIRED = False
LFS_SHIPPING_PHONE_REQUIRED = False

LFS_PRICE_CALCULATORS = [
    ['lfs.gross_price.GrossPriceCalculator', _(u'Price includes tax')],
    ['lfs.net_price.NetPriceCalculator', _(u'Price excludes tax')],
]

LFS_SHIPPING_METHOD_PRICE_CALCULATORS = [
    ["lfs.shipping.GrossShippingMethodPriceCalculator", _(u'Price includes tax')],
    ["lfs.shipping.NetShippingMethodPriceCalculator", _(u'Price excludes tax')],
]

LFS_UNITS = [
    u"l",
    u"m",
    u"qm",
    u"cm",
    u"lfm",
    u"Package",
    u"Piece",
    u"",
    u"",
    u"",
]

LFS_PRICE_UNITS = LFS_BASE_PRICE_UNITS = LFS_PACKING_UNITS = LFS_UNITS

LFS_LOG_FILE = DIRNAME + "/../lfs.log"
LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "datefmt": "%a, %d %b %Y %H:%M:%S",
        },
    },
    "handlers": {
         "console":{
            "level":"DEBUG",
            "class":"logging.StreamHandler",
            "formatter": "verbose",
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': LFS_LOG_FILE,
            'mode': 'a',
        },
    },
    "loggers": {
        "default": {
            "handlers": ["logfile", "console"],
            "level": "DEBUG",
            "propagate": False,
        },
    }
}

REVIEWS_SHOW_PREVIEW = False
REVIEWS_IS_NAME_REQUIRED = False
REVIEWS_IS_EMAIL_REQUIRED = False
REVIEWS_IS_MODERATED = False




# Django-carousel

SOUTH_MIGRATION_MODULES = {
        'easy_thumbnails': 'easy_thumbnails.south_migrations',
    }

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

THUMBNAIL_BASEDIR='thumbs'
# heroku setting

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )


## Amazon S3 Settings
if not SWITCH:       
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    #STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    #AWS_S3_SECURE_URLS = False       # use http instead of https
    AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = 'zentec-momo'
    #S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    #STATIC_URL = S3_URL    
    AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2020 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
    }
    THUMBNAIL_DEFAULT_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Sendgrid

    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

## Django compressor for S3 Settings
# if not DEBUG:
#   COMPRESS_URL='http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#   STATIC_URL=COMPRESS_URL
#   COMPRESS_STORAGE='Storage.CachedS3BotoStorage'
#   STATICFILES_STORAGE = COMPRESS_STORAGE
#   COMPRESS_ROOT = STATIC_ROOT


try:
    from local_settings import *
except ImportError:
    pass
