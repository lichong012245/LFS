Django-LFS bootstrap
====================

A simple and pythonic way to build your django-lfs shop.

Clone django-lfs-bootstrap
--------------------------

	$ git clone https://github.com/MrTango/django-lfs-bootstrap.git shop

The you have the following structure:

	./shop
	├── lfs_project
	│   ├── __init__.py
	│   ├── local_settings.py_tmpl
	│   ├── manage.py
	│   ├── settings.py
	│   └── urls.py
	├── README.md
	└── requirements.txt


Create virtualenv
-----------------

Its recommended to use virtalenv to avoid conflicts. If you don't know virtualenv please read this: http://pypi.python.org/pypi/virtualenv/.

Install django and django-lfs
-----------------------------

	$ pip install -r requirements.txt

Make your settings
------------------

The settings are in settings.py and local_settings.py. You can override every from settings.py in you local_settings.py.
As a starting point you can just copy the local_settings.py_tmpl

	$ cp local_settings.py_tmpl local_settings.py

Then define your database and language aso in local_settings.py or settings.py
You can override every from settings.py in you local_settings.py

Sync th database
----------------

	$ ./manage.py syncdb

Initialize lfs
--------------

	$ ./manage.py lfs_init

Collect static files
--------------------

	$ ./manage.py collectstatic

Start your shop:
----------------

	$ ./manage.py runserver 

or

	$ ./manage.py runserver 127.0.0.1:8080


Of course, you can use any WSGI server to run your shop now. 

