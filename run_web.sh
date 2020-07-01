#!/bin/sh

# Crear migraciones de BD
python manage.py makemigrations

# Aplicar las migraciones de BD
python manage.py migrate

# Inciar el servidor
python manage.py runserver 0.0.0.0:8000
