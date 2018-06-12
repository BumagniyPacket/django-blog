#!/bin/sh
python /code/manage.py migrate
python /code/manage.py collectstatic --noinput
gunicorn -c /code/gunicorn.py core.wsgi