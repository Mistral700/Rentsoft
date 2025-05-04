#!/bin/sh

python manage.py wait_db
python manage.py migrate
python manage.py create_default_superuser
python manage.py seed_initial_data
python manage.py runserver 0.0.0.0:8000