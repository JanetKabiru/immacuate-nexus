#!/usr/bin/env bash

python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
