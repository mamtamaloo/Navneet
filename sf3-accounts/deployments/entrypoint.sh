#!/usr/bin/env bash
echo "Gunicorn server starting"
gunicorn -c src/core/gunicorn.conf.py main:app
echo "Welcome"
