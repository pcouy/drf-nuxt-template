cd /django_app
/home/djangouser/.local/bin/poetry install --with dev
/home/djangouser/.local/bin/poetry run python manage.py migrate
/home/djangouser/.local/bin/poetry run python manage.py collectstatic --noinput
/home/djangouser/.local/bin/poetry run python manage.py runserver_plus --nostatic 0.0.0.0:8000
