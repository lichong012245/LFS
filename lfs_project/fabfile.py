import os
from fabric.api import env,run, local

env.host=['momo-clothing.herokuapp.com',]

def push_to_heroku():
	local('git push momo master')
	local('heroku logs --app momo-clothing')
	local('heroku run python manage.py validate --app momo-clothing')
	local('heroku run python manage.py syncdb --app momo-clothing')
	local('heroku run python manage.py migrate --app momo-clothing')