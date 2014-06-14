"""
WSGI config for zen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lfs_project.settings")


try:
	from django.core.wsgi import get_wsgi_application
	from dj_static import Cling
	application = Cling(get_wsgi_application())
except ImportError:
	from dj_static import Cling
	import django.core.handlers.wsgi
	application = Cling(django.core.handlers.wsgi.WSGIHandler())



try:
	from wsgi_local import *
except ImportError:
	pass