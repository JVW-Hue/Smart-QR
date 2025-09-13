#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip setuptools wheel
pip install Django==4.2.7
pip install qrcode==7.4.2
pip install --no-build-isolation Pillow==10.4.0
pip install stripe==7.8.0
pip install python-decouple==3.8
pip install gunicorn==21.2.0
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput