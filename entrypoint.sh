#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noi

uvicorn config.asgi:application --host 0.0.0.0 --port 8000
