#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations cargos
python manage.py migrate cargos
python manage.py load_locations
python manage.py load_cars
python manage.py runserver 0:8000
