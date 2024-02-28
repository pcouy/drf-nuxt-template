yes | adduser --uid 1000 --disabled-password djangouser
apt-get update && apt-get install -y curl sudo && curl -sSL https://install.python-poetry.org | sudo -u djangouser python3 -
cd /django_app
sudo -u djangouser /home/djangouser/.local/bin/poetry install --without dev
