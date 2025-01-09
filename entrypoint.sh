#!/bin/sh

dockerd &

while ! docker info > /dev/null 2>&1; do
    sleep 1
done

python3 -m venv /venv
source /venv/bin/activate
pip3 install --no-cache --upgrade pip setuptools
pip3 install -r requirements.txt

export FLASK_APP=app.py
export FLASK_RUN_HOST=0.0.0.0

echo $CTF_FLAG > /inception/flag.txt

gunicorn --bind 0.0.0.0:5000 wsgi:app --workers 8

echo Looping in /dev/null. Press Ctrl+C to break out of loop.
tail -f /dev/null

