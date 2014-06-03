# -*- coding: utf-8 -*-

# python imports
import os

DIRNAME = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TESTING = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DIRNAME + '/lfs.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Make this unique, and don't share it with anybody!
SECRET_KEY = '+0zsw5n@v7*rhl6r6ufqhoc6jlqq0f-u8c+gh(hjb+_jmg@rh6'

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en'

DEFAULT_FROM_EMAIL = 'your_email@domain.com'

EMAIL_HOST = "localhost"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    "mytheme",      
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
    'lfs.core',
    "lfs.tests",    
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
    'lfs.portlet',
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
    "lfstheme",
    'postal',
    'paypal.standard.ipn',
    'paypal.standard.pdt', 
    'south',
    'hvad',
    'paintstore',
    'image_cropping',
    'easy_thumbnails',
    'django_carousel',
    # If you're using Django 1.6.x or earlier
    'debug_toolbar',
)

# DEBUG_TOOLBAR_PATCH_SETTINGS = False

# MIDDLEWARE_CLASSES += [
#     # ...
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
#     # ...
# ]