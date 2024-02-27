FROM python:3.11-slim
WORKDIR /django_app
ENV PATH="${PATH}:/home/djangouser/.local/bin"
COPY docker-utils/docker-install.sh /
COPY pyproject.toml /django_app
COPY poetry.lock /django_app
RUN bash /docker-install.sh
