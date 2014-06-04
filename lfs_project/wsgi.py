"""
WSGI config for zen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
from lfs_project.settings import DEBUG
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lfs_project.settings")

##if DEBUG:
   #from django.core.wsgi import get_wsgi_application
   #application = get_wsgi_application()
   #import django.core.handlers.wsgi
   #application = django.core.handlers.wsgi.WSGIHandler()

#if not DEBUG:
from dj_static import Cling
import django.core.handlers.wsgi
application = Cling(django.core.handlers.wsgi.WSGIHandler())

try:
	from wsgi_local import *
except ImportError:
	pass