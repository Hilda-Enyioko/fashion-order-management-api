#!/bin/bash
source myenv/bin/activate
gunicorn fashion_api.wsgi --log-file -
