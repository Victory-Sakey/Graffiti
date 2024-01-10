#!/bin/bash

echo "Current working directory: $(pwd)"
ls -al  # Print the content of the current directory

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput
