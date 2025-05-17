#!/usr/bin/env sh
set -e

# Activate the virtualenv
. /home/appuser/app/venv/bin/activate

# Run database migrations
echo ">>> Applying Alembic migrations…"chmod
alembic upgrade head

# Finally, launch Gunicorn (or flask)
echo ">>> Starting Gunicorn…"
exec gunicorn --bind 0.0.0.0:8000 wsgi:app --workers 4 --worker-class sync