#!/bin/bash
# entrypoint.sh

# Exit immediately if a command exits with a non-zero status
set -e

# Run migrations (optional, if needed)
python manage.py migrate

# Collect static files (optional, if needed)
python manage.py collectstatic --noinput

# Start the server
python manage.py runserver 0.0.0.0:8000
