#!/bin/sh

uvicorn config.asgi:application --host 0.0.0.0 --port 8000
