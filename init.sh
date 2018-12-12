#!/bin/bash
set -e

echo "Starting SSH ..."
service ssh start

cd /
python django-excellence-gls/manage.py runserver 0.0.0.0:8000
