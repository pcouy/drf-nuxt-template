cd /django_app
/home/djangouser/.local/bin/poetry install --without dev
/home/djangouser/.local/bin/poetry run python manage.py migrate
/home/djangouser/.local/bin/poetry run python manage.py collectstatic --noinput
/home/djangouser/.local/bin/poetry run gunicorn -w 4 {{ project_name }}.wsgi --bind 0.0.0.0:8000
